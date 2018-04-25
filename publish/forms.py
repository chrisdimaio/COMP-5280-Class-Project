from django import forms

from .models import Post

class PublishWordForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('word', 'description',)



class SearchForm(forms.Form):
    query_string = forms.CharField(label='', max_length=100)