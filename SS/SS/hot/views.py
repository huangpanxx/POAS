# Create your views here.
# -*- coding: utf-8 -*-
from hot.models import Lexical,Lex_Doc,Doc
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
import time

def hot(request):
    local_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    field1 = request.POST.get('field', '')
    type = request.POST.get('type', '')
    if type == "Today":
        words = Lexical.objects.raw("select * from Lex where field = %s and date = '2012-8-1' group by total_weight desc limit 10",[field1] )
#    words = Lexical.objects.filter(field = field1).filter(date = u‘2012-8-1’).order_by("-total_weight")[:word_size]
    else:
        words = Lexical.objects.raw("select * from Lex where field = %s and date = '2012-8-1' group by total_weight desc limit 10",[field1] )
    return render_to_response('hot/hot.html',
                              {'words':words,
                               'field':field1
                               },
                              context_instance=RequestContext(request))
    
def hot_detail(request,word_id):
    news = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '新闻' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight limit 10",[word_id])
    blog = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '博客' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight linit 10",[word_id])
    bbs = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '论坛' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight limit 10",[word_id])
    return render_to_response('hot/hot_detail.html',
                              {'news':news,
                               'blog':blog,
                               'bbs':bbs
                               },
                              context_instance=RequestContext(request))
        