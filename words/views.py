from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Word


# Create your views here.

def index(request):
    array = Word.objects.all()
    return render_to_response('words/index.html', {'my_array': array})

def word_view(request, id):
    w = Word.objects.get(pk = id)
    return render_to_response('words/word_view', {'word' : w})