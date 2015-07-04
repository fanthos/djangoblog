from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.views.decorators.cache import cache_page
from django.core.exceptions import ObjectDoesNotExist
from aboutme.models import *

# Create your views here.
#@cache_page(15)
def main(request):
	req1=request.path.lower()
	if req1 == "/": req1 = "/home"
	try:
		pageobj=Pages.objects.get(uri=req1)
		t = loader.get_template('home.html')
		c = Context({'title': pageobj.title, 'text_html': pageobj.text_html})
		resp=HttpResponse(t.render(c))
		return resp

	except ObjectDoesNotExist as e:
		raise Http404
	except:
		raise
		raise Http403

@cache_page(15)
def blog(request):
	req1=request.path
	resp=HttpResponse(req1)
	return resp
