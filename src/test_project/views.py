from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def test_view(request):
	return HttpResponse("some stuff")

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	obj = get_object_or_404()