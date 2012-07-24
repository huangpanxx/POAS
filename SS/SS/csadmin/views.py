# Create your views here.
#coding:utf8
from .models import settings
from django.http import HttpResponse
from .utils import jsonrpc_call_server
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response

def address(request):
    if request.method == "POST":
        pass
    return render_to_response('address.html',
                               {'settings':settings},
                               context_instance = RequestContext(request)
                               )

def cache(request):
    data = jsonrpc_call_server('cache', 'keys', pattern='*')
    return HttpResponse(data)

def test(request):
    t = get_template('login_bar_test.html')
    c = Context(locals())
    resp = HttpResponse(t.render(c))
    return resp
    
    
