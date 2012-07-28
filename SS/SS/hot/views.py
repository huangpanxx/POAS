# Create your views here.
from hot.models import Lexical
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response

def hot(request,word_size = 10):
    words = Lexical.objects.raw('SELECT * FROM hot_lexical group by total_weight desc limit %s',word_size)
    return render_to_response('hot/hot.html',
                              {'words':words,
                               },
                              context_instance=RequestContext(request))