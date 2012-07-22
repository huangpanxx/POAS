'''
Created on 2012-7-18

@author: snail
'''
from twisted.application.service import Application
from twisted.application.internet import TimerService, TCPServer #@UnresolvedImport
from twisted.web import server
from twisted.python import log

from scrapyd.interfaces import IEggStorage, IPoller, ISpiderScheduler, IEnvironment
from scrapyd.launcher import Launcher
from scrapyd.eggstorage import FilesystemEggStorage
from scrapyd.scheduler import SpiderScheduler
from scrapyd.poller import QueuePoller
from scrapyd.environ import Environment
from scrapyd.website import Root
from scrapyd.config import Config
from scrapy.utils.misc import load_object

def configRoot(root,config):
    config = Config()
    _services = config.get('services', {})

    #services = eval(_services)
    #for key,value in services.items():
        #service = load_object(value)
    #    root.putChild(key, service(root))
        
    root.update_projects()
    return root

def application(config):
    app = Application("Scrapyd")
    http_port = config.getint('http_port', 6800)

    poller = QueuePoller(config)
    eggstorage = FilesystemEggStorage(config)
    scheduler = SpiderScheduler(config)
    environment = Environment(config)

    app.setComponent(IPoller, poller)
    app.setComponent(IEggStorage, eggstorage)
    app.setComponent(ISpiderScheduler, scheduler)
    app.setComponent(IEnvironment, environment)

    launcher = Launcher(config, app)
    timer = TimerService(5, poller.poll)
    root = Root(config,app)
    root = configRoot(root,config)
    
    webservice = TCPServer(http_port, server.Site(root))
    log.msg("Scrapyd web console available at http://localhost:%s/" % http_port)

    launcher.setServiceParent(app)
    timer.setServiceParent(app)
    webservice.setServiceParent(app)

    return app
