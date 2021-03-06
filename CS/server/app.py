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
from scrapy.utils.misc import load_object

def configRoot(root, config):
	_services = config.get('services', '{}') 
	try:
		services = eval(_services)
	except Exception, e:
			log.msg('services config is wrong:%s' % (e,))
			exit(1)

	for key, value in services.items():
		try:
			print value
			service = load_object(value)
			root.putChild(key, service(root))
			log.msg('load service:%s' % value)
		except Exception, e:
			log.msg('load %s error:%s' % (value, e))
			exit(1)

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
	root = Root(config, app)
	root = configRoot(root, config)
	
	webservice = TCPServer(http_port, server.Site(root))
	log.msg("Scrapyd web console available at http://localhost:%s/" % http_port)

	launcher.setServiceParent(app)
	timer.setServiceParent(app)
	webservice.setServiceParent(app)

	return app
