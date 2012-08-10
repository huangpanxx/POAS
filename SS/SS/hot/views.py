# Create your views here.
# -*- coding: utf-8 -*-
from hot.models import Lexical,Lex_Doc,Doc,Date
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
import time

def hot(request):
    local_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    field1 = request.POST.get('field', '')
    type = request.POST.get('type', '')
    fields = Doc.objects.raw("select * from Document group by field limit 20")
    if type == "Today":
        words = Lexical.objects.raw("select * from Lex where field = %s and date = '2012-8-1' group by total_weight desc limit 10",[field1] )
#    words = Lexical.objects.filter(field = field1).filter(date = u‘2012-8-1’).order_by("-total_weight")[:word_size]
    else:
        words = Lexical.objects.raw("select * from Lex where field = %s and date = '2012-8-1' group by total_weight desc limit 10",[field1] )
    return render_to_response('hot/hot.html',
                              {'words':words,
                               'field':field1,
                               'fields':fields
                               },
                              context_instance=RequestContext(request))
    
def hot_detail(request,word_id):
    value = Lexical.objects.filter(id = word_id)[0]
    news = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '新闻' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight limit 10",[word_id])
    blog = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '博客' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight limit 10",[word_id])
    bbs = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '论坛' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight limit 10",[word_id])
    return render_to_response('hot/hot_detail.html',
                              {'value':value,
                               'news':news,
                               'blog':blog,
                               'bbs':bbs,
                               },
                              context_instance=RequestContext(request))
    
def transport(request):
    value = request.GET.get('value', '')
    tmp_websites = Doc.objects.raw("select * from Document group by website")
    websites = []
    for website in tmp_websites:
        websites.append(website.website)
    dates = []
    date = 6
    tmp_date = Date.objects.raw("select * from date where datediff(curdate(),date) <= %s",[date])
    for tmp in tmp_date:
        dates.append(tmp.date)
    results = []
    while date >= 0:
        tmp_res = {}
        for website in websites:
            tmp_res[website] = 0
        words = Lexical.objects.raw("select * from Lex where value = %s and datediff(curdate(),date) = %s",[value,date])
        for word in words:
            docs = Doc.objects.raw("select Document.id,Document.website,count(Document.website) as num from Document,Lex_Doc where Document.id = Lex_Doc.Doc_id and Lex_Doc.Lex_id = %s group by Document.website",[word.id])
            for doc in docs:
                tmp_res[doc.website] += doc.num
        results.append(tmp_res)
        date -= 1    
    return render_to_response('hot/transport.html',
                              {'results':results,
                               'dates':dates,
                               'websites':websites
                               },
                              context_instance=RequestContext(request))