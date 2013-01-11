from calais import Calais
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson as json

def index(request):    
    t = "index.html"
    c = { 'title' : 'Jigsaw'}
    return render_to_response(t, c,
                               context_instance=RequestContext(request))

def analyze(request):
    API_KEY = 'kgmykdr862hdfhkzkuchnxkc'
    calais = Calais(API_KEY, 'python')
    try:
        result = calais.analyze(request.POST['content'])
        if result:
            return HttpResponse(json.dumps(result.get_json_entities()),
                                mimetype="application/json")
        else:
            return HttpResponse(json.dumps(""),
                                mimetype="application/json")
    except(KeyError):
        return HttpResponse(json.dumps(""),
                                mimetype="application/json")
