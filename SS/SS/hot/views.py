# Create your views here.
# -*- coding: utf-8 -*-
from hot.models import Lexical,Lex_Doc,Doc,Date,Field
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
import time
from function import rank

def compute(request):
    field1 = request.POST.get('field', '')
    type = request.POST.get('type', '')
    fields = Field.objects.raw("select * from field")
    if type == 'today':
        words = Lexical.objects.raw("select * from Lex where field = %s and datediff('2012-8-10',date) = 0 group by total_weight desc limit 10",[field1])
        words_y = Lexical.objects.raw("select * from Lex where field = %s and datediff('2012-8-10',date) = 1 group by total_weight desc limit 10",[field1])
        delta = rank(words,words_y)
#    words = Lexical.objects.filter(field = field1).filter(date = u‘2012-8-1’).order_by("-total_weight")[:word_size]
    else:
        words = Lexical.objects.raw("select *,sum(total_weight) as sum from lex where datediff('2012-8-10',date) <= 6 and field = %s group by value order by sum desc limit 10;",[field1] )
        words_y = words = Lexical.objects.raw("select *,sum(total_weight) as sum from lex where datediff('2012-8-10',date) > 6 and datediff('2012-8-10',date) <= 13 and field = %s group by value order by sum desc limit 10;",[field1] )
        delta = rank(words,words_y)        
    
    results = [[]]
    i = 0
    for word in words:
        tmp = []
        tmp.append(i + 1)
        tmp.append(word.value)
        tmp.append(delta[i])
        tmp.append(word.total_weight)
        tmp.append(word.id)
        results.append(tmp)
        i += 1
    return {
            'words':words,
            'fields':fields,
            'results':results
            }
def hot(request):
    return render_to_response('hot/hot.html',
                            compute(request),
                              context_instance=RequestContext(request))
    
def hot_detail(request,word_id):
    value = Lexical.objects.filter(id = word_id)[0]
    news = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '新闻' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight desc limit 10",[word_id])
    blog = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '博客' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight desc limit 10",[word_id])
    bbs = Lex_Doc.objects.raw("select Document.* from Lex_Doc,Document where Document.id = Lex_Doc.Doc_id and Document.source = '论坛' and Lex_Doc.Lex_id = %s group by Lex_Doc.weight desc limit 10",[word_id])
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
    choose_web = []
    for website in websites:
        get_value = request.POST.get(website, '')
        if get_value != "":
            choose_web.append(request.POST.get(website, ''))
    dates = []
    date = 6
    tmp_date = Date.objects.raw("select * from date where datediff('2012-8-10',date) <= %s",[date])
    for tmp in tmp_date:
        dates.append(tmp.date)
    results = []
    while date >= 0:
        tmp_res = {}
        for website in choose_web:
            tmp_res[website] = 0
        words = Lexical.objects.raw("select * from Lex where value = %s and datediff('2012-8-10',date) = %s",[value,date])
        for word in words:
            docs = Doc.objects.raw("select Document.id,Document.website,count(Document.website) as num from Document,Lex_Doc where Document.id = Lex_Doc.Doc_id and Lex_Doc.Lex_id = %s group by Document.website",[word.id])
            for doc in docs:
                if doc.website in choose_web:
                    tmp_res[doc.website] += doc.num
        results.append(tmp_res)
        date -= 1  
    p = []
    for website in choose_web:
        i = 0
        r = []
        q = []
        while i < len(results):
            q.append(results[i][website])
            i += 1
        r.append(website)
        r.append(q)
        p.append(r)
    return render_to_response('hot/transport.html',
                              {'results':p,
                               'dates':dates,
                               'websites':websites,
                               'website':choose_web
                               },
                              context_instance=RequestContext(request))