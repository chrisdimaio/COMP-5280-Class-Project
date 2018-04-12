from django.http import HttpResponse
from .models import word, users_def
from django.template import loader
from django.shortcuts import render
from utilities import dictionary_request
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    all_words = word.objects.all()
    context = {}
    return render(request, 'word_display/index.html', context)

def wordDef(request, word_id):
    return render(request, 'word_display/wordDef.html')

def dict_search(request):
    word_value = request.POST.get('word_value')
    definition = dictionary_request(word_value)
    #definition = "hello"
    try:
        word_entry = word.objects.get(wordEntry=word_value)
    except ObjectDoesNotExist:
        word_entry = word()
        word_entry.wordEntry = word_value
        word_entry.save()
    context = {
        'word_value' : word_value,
        'definition' : definition,
        'word_entry' : word_entry
    }
    return render(request, 'word_display/wordDef.html', context)

def add_def(request):
    #add def to database
    word_value = request.POST.get('word_value')
    u_def = request.POST.get('user_def')
    ud = users_def()
    word_entry = word.objects.get(wordEntry=word_value)
    ud.wordEntry = word_entry
    ud.userDef = u_def
    ud.save()
    return render(request, 'word_display/index.html', {'word_value': word_value})