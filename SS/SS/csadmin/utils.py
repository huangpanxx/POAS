'''
Created on 2012-7-19

@author: snail
'''
#!/usr/bin/env python
"""
Example script to control a Scrapy server using its JSON-RPC web service.

It only provides a reduced functionality as its main purpose is to illustrate
how to write a web service client. Feel free to improve or write you own.

Also, keep in mind that the JSON-RPC API is not stable. The recommended way for
controlling a Scrapy server is through the execution queue (see the "queue"
command).

"""

import urllib
from urlparse import urljoin
from scrapy.utils.jsonrpc import jsonrpc_client_call
from .models import settings
import json

def get_wsurl_server(path):
    host = settings.server_address
    port = settings.server_port
    return urljoin("http://%s:%s/"% (host, port), path)

def jsonrpc_call_server(path, method, *args, **kwargs):
    url = get_wsurl_server(path)
    return jsonrpc_client_call(url, method, *args, **kwargs)

def json_get_server(path):
    url = get_wsurl_server(path)
    return json.loads(urllib.urlopen(url).read())


def get_wsurl_spider(path):
    host = settings.server_address
    port = settings.spider_port
    return urljoin("http://%s:%s/"% (host, port), path)

def jsonrpc_call_spider(path, method, *args, **kwargs):
    url = get_wsurl_server(path)
    return jsonrpc_client_call(url, method, *args, **kwargs)

def json_get_spider(path):
    url = get_wsurl_server(path)
    return json.loads(urllib.urlopen(url).read())
