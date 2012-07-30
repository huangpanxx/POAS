# Create your views here.
from hot.models import Lexical
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response

def hot(request,word_size = 10):
    field = request.POST.get('field', '')
    type = request.POST.get('type', '')
    if type == "Today":
        words = Lexical.objects.raw('SELECT * FROM Lex where field = %s and date = now() group by total_weight desc limit %s',field,word_size)
    else:
        words = Lexical.objects.raw('SELECT * FROM Lex where field = %s and group by total_weight desc limit %s',field,word_size)
    return render_to_response('hot/hot.html',
                              {'words':words,
                               },
                              context_instance=RequestContext(request))