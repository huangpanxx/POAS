# Create your views here.
from hot.models import Lexical,Lex_Doc,Doc
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
import time

def hot(request,word_size = 10):
    local_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    field1 = request.POST.get('field', '')
    type = request.POST.get('type', '')
#    if type == "Today":
    words = Lexical.objects.filter(field = field1).filter(date = local_date).order_by("-total_weight")[:word_size]
#    else:
#        words = Lexical.objects.all()
    return render_to_response('hot/hot.html',
                              {'words':words,
                               'length':words.count()
                               },
                              context_instance=RequestContext(request))
    
def hot_detail(request,word_id):
    news = Lex_Doc.objects.filter(Lex_id = word_id).filter(field = "新闻").order_by("-weight")
    if news.size() > 10:
        news = news[:10]
    blog = Lex_Doc.objects.filter(Lex_id = word_id).filter(field = "博客").order_by("-weight")
    if blog.size() > 10:
        blog = blog[:10]
    bbs = Lex_Doc.objects.filter(Lex_id = word_id).filter(field = "论坛").order_by("-weight")
    if bbs.count() > 10:
        bbs = bbs[:10]
    return render_to_response('hot/hot_detail.html',
                              {'news':news,
                               'blog':blog,
                               'bbs':bbs
                               },
                              context_instance=RequestContext(request))
        