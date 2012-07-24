"""This module can be used to execute Scrapyd from a Scrapy command"""

import sys
import os
from cStringIO import StringIO

from twisted.python import log
from twisted.internet import reactor
from twisted.application import app


from scrapyd import get_application
from scrapyd.config import Config

from scrapy.utils.project import project_data_dir

def _get_config(config_file):
    datadir = os.path.join(project_data_dir(), '.scrapy', 'scrapyd')
    conf = {
        'eggs_dir': os.path.join(datadir, 'eggs'),
        'logs_dir': os.path.join(datadir, 'logs'),
        'dbs_dir': os.path.join(datadir, 'dbs'),
    }
    for k in ['eggs_dir', 'logs_dir', 'dbs_dir']: # create dirs
        d = conf[k]
        if not os.path.exists(d):
            os.makedirs(d)
    scrapyd_conf = """
[scrapyd]
eggs_dir = %(eggs_dir)s
logs_dir = %(logs_dir)s
dbs_dir  = %(dbs_dir)s
    """ % conf
    conf_list = [StringIO(scrapyd_conf),StringIO(open(config_file).read())]
    return Config(extra_sources=conf_list)

def execute(config_file):
    config = _get_config(config_file)
    log.startLogging(sys.stderr)
    application = get_application(config)
    app.startApplication(application, False)
    reactor.run() #@UndefinedVariable
    
