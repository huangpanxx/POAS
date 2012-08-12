# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from home.models import Item,Tendency,Classifyrule,Field,Sourcetype
from hot.models import Doc

def render(html_path, request, dic_data):
    return render_to_response(html_path, dic_data,
        context_instance=RequestContext(request))


def classify(request):
    c = request.GET.get('c', '')
    if not c:
        news = Item.objects.raw("select item.id ,item.title,item.url,item.publish_datetime from item, ClassifyRule, Field, SourceType,Tendency where ClassifyRule.source_type_id=SourceType.id and ClassifyRule.field_id=Field.id and ClassifyRule.id=item.classify_rule_id and sourcetype.name = '新闻' and Tendency.item_id = item.id and tendency.tendency_value < -10 order by item.publish_datetime desc limit 6");
        blogs = Item.objects.raw("select item.id,item.title,item.url,item.publish_datetime from item, ClassifyRule, Field, SourceType,Tendency where ClassifyRule.source_type_id=SourceType.id and ClassifyRule.field_id=Field.id and ClassifyRule.id=item.classify_rule_id and sourcetype.name = '博客' and Tendency.item_id = item.id and tendency.tendency_value < -10 order by item.publish_datetime desc limit 6");
        bbs = Item.objects.raw("select item.id,item.title,item.url,item.publish_datetime from item, ClassifyRule, Field, SourceType,Tendency where ClassifyRule.source_type_id=SourceType.id and ClassifyRule.field_id=Field.id and ClassifyRule.id=item.classify_rule_id and sourcetype.name = '论坛' and Tendency.item_id = item.id and tendency.tendency_value < -10 order by item.publish_datetime desc limit 6");
        return render('classify/classify.html', request, {'news':news,'blogs':blogs,'bbs':bbs})
    if c:
        results = Item.objects.raw("select item.id,item.title,item.url ,item.publish_datetime from item, ClassifyRule, Field, SourceType,Tendency where ClassifyRule.source_type_id=SourceType.id and ClassifyRule.field_id=Field.id and ClassifyRule.id=item.classify_rule_id and sourcetype.name = %s and Tendency.item_id = item.id and tendency.tendency_value < -10 order by item.publish_datetime desc limit 25",[c]);
        return render('classify/more.html', request, {'results':results,'c':c})


def news(request):
    results = Item.objects.raw("select Item.id,Item.title,item.url,item.publish_datetime,site.name from item,site,spider,classifyrule,tendency where item.classify_rule_id = classifyrule.id and spider.id = classifyrule.spider_id and spider.site_id = site.id and tendency.item_id = item.id and tendency.tendency_value < -10 order by item.publish_datetime desc limit 8;")

    news = []
    new_1 = Doc.objects.raw("select *,count(*) as num from document where source = '新闻' and datediff('2012-8-10',date) = 0")
    new_2 = Doc.objects.raw("select *,count(*) as num from document where source = '新闻' and datediff('2012-8-10',date) = 1")
    new_3 = Doc.objects.raw("select *,count(*) as num from document where source = '新闻' and datediff('2012-8-10',date) <= 6")
    new_4 = Doc.objects.raw("select *,count(*) as num from document where source = '新闻' and datediff('2012-8-10',date) <=30")
    for new in new_1:
        news.append(new.num)
    for new in new_2:
        news.append(new.num)
    for new in new_3:
        news.append(new.num)
    for new in new_4:
        news.append(new.num)
        
    blogs = []
    blog_1 = Doc.objects.raw("select *,count(*) as num from document where source = '博客' and datediff('2012-8-10',date) = 0")
    blog_2 = Doc.objects.raw("select *,count(*) as num from document where source = '博客' and datediff('2012-8-10',date) = 1")
    blog_3 = Doc.objects.raw("select *,count(*) as num from document where source = '博客' and datediff('2012-8-10',date) <= 6")
    blog_4 = Doc.objects.raw("select *,count(*) as num from document where source = '博客' and datediff('2012-8-10',date) <=30")
    for blog in blog_1:
        blogs.append(blog.num)
    for blog in blog_2:
        blogs.append(blog.num)
    for blog in blog_3:
        blogs.append(blog.num)
    for blog in blog_4:
        blogs.append(new.num)
        
    bbs = []
    bbs_1 = Doc.objects.raw("select *,count(*) as num from document where source = '论坛' and datediff('2012-8-10',date) = 0")
    bbs_2 = Doc.objects.raw("select *,count(*) as num from document where source = '论坛' and datediff('2012-8-10',date) = 1")
    bbs_3 = Doc.objects.raw("select *,count(*) as num from document where source = '论坛' and datediff('2012-8-10',date) <= 6")
    bbs_4 = Doc.objects.raw("select *,count(*) as num from document where source = '论坛' and datediff('2012-8-10',date) <=30")
    for bb in bbs_1:
        bbs.append(bb.num)
    for bb in bbs_2:
        bbs.append(bb.num)
    for bb in bbs_3:
        bbs.append(bb.num)
    for bb in bbs_4:
        bbs.append(bb.num)
        
    return render('news/news.html',request,{'results':results,'news':news,'bbs':bbs,'blogs':blogs})

def competitor(request):
    return render('competitor/competitor.html', request, {})


