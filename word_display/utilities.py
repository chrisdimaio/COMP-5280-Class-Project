import requests
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import word, users_def


def dictionary_request(word_id):
    app_id = '7b58b972'
    app_key = 'fb9496a24aaffb6de1b5892fe681d445'

    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id':app_id, 'app_key': app_key})
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