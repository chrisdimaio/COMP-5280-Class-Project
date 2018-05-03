from django.http import HttpResponse
from .models import word, users_def
from django.template import loader
from django.shortcuts import render
# from utilities import dictionary_request, add_def_to_db
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import requests
import json

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'word_display/signup.html'

def index(request):
    context = {}
    return render(request, 'word_display/index.html', context)

def wordDef(request):
    return render(request, 'word_display/wordDef.html')

def dict_search(request):
    word_value = request.POST.get('word_value')
    definition = dictionary_request(word_value)
    print "here", definition
    word_value = word_value.lower()
    try:
        word_entry = word.objects.get(wordEntry=word_value)
    except ObjectDoesNotExist:
        word_entry = word()
        word_entry.wordEntry = word_value
        word_entry.wordDef = definition
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
    add_def_to_db(word_value, u_def)
    word_entry = word.objects.get(wordEntry=word_value)
    context = {
        'word_value' : word_entry.wordEntry,
        'definition' : word_entry.wordDef,
        'word_entry' : word_entry
    }
    return render(request, 'word_display/wordDef.html', context)


def about_us(request):
    return render(request, "word_display/about_us.html")

def up_vote(request):
    key = request.POST.get('key')
    u_def = users_def.objects.get(pk=key)
    u_def.def_votes = u_def.def_votes + 1
    u_def.save()
    word_value = request.POST.get('word_value')
    word_entry = word.objects.get(wordEntry=word_value)
    context = {
        'word_value' : word_entry.wordEntry,
        'definition' : word_entry.wordDef,
        'word_entry' : word_entry
    }
    return render(request, 'word_display/wordDef.html', context)

def down_vote(request):
    key = request.POST.get('key')
    u_def = users_def.objects.get(pk=key)
    u_def.def_votes = u_def.def_votes - 1
    u_def.save()
    word_value = request.POST.get('word_value')
    word_entry = word.objects.get(wordEntry=word_value)
    context = {
        'word_value' : word_entry.wordEntry,
        'definition' : word_entry.wordDef,
        'word_entry' : word_entry
    }
    return render(request, 'word_display/wordDef.html', context)

def user_def(request, word_value):
    context = {
        "word_value": word_value
    }
    return render(request, 'word_display/user_def.html', context)


def dictionary_request(word_id):
    app_id = '7b58b972'
    app_key = 'fb9496a24aaffb6de1b5892fe681d445'

    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id':app_id, 'app_key': app_key})

    if r.status_code == 404:
        retValue = " WORD NOT FOUND"
    else:
        result = json.loads(r.text)
        retValue =  result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    return retValue

def add_def_to_db(word_value, u_def):
    ud = users_def()
    word_entry = word.objects.get(wordEntry=word_value)
    ud.wordEntry = word_entry
    ud.userDef = u_def
    ud.save()
    return