from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
# from .apps.polls.models import poll, comment


def home(request):
    return render(request, 'home.html')
