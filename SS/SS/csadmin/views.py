# Create your views here.
#coding:utf8
from .models import settings
from django.http import HttpResponse
from .utils import jsonrpc_call_server
from django.template.loader import get_template
from django.template.context import Context

def address(request):
    addr = settings.server_address
    return HttpResponse(addr)

def cache(request):
    data = jsonrpc_call_server('cache','keys',pattern='*')
    return HttpResponse(data)

def test(request):
    t = get_template('login_bar_test.html')
    c = Context(locals())
    resp = HttpResponse(t.render(c))
    return resp
    
    