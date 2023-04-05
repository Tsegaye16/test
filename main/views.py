from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def index(response, id):
	return HttpResponse("<h1>%s</h1>",%id)

