# Create your views here.
#coding:utf8
from .models import settings
from django.http import HttpResponse
from .utils import jsonrpc_call_server

def Address(request):
    addr = settings.server_address
    return HttpResponse(addr)

def Cache(request):
    data = jsonrpc_call_server('cache','keys',pattern='*')
    return HttpResponse(data)
    