# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render(html_path, request, dic_data):
    return render_to_response(html_path, dic_data,
        context_instance=RequestContext(request))


def classify(request):
    c = request.GET.get('c', '')
    if not c:
        return render('classify/classify.html', request, {})
    if c:
        return render('classify/classify.html', request, {})


def news(request):
    return render('news/news.html', request, {})


