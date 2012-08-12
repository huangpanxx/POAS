# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render(html_path, request, dic_data):
    return render_to_response(html_path, dic_data,
        context_instance=RequestContext(request))


def classify(request):
    return render('classify/classify.html', request,{})


