from django import forms
from .models import word

class Meta:
    model = word
    fields = ('word',)