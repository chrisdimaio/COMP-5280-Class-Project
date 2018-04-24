from django import forms

from .models import Post

class PublishWordForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('word', 'description',)