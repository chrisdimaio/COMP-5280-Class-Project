from django.shortcuts import render
from .forms import PublishWordForm
from django.views.generic import TemplateView
from django.utils import timezone

class PublishView(TemplateView):
    template_name = 'publish/publish_edit.html'

    def get(self, request, *args, **kwargs):
        form = PublishWordForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PublishWordForm(request.POST)
        if form.is_valid():
            form.save()
            word = form.cleaned_data['word']
            description = form.cleaned_data['description']
            form = PublishWordForm()
            return render(request, self.template_name, {'form': form})

# def publish_new(request):

    # if request.method == "POST":
    #     form = PublishWordForm()
    #     if form.is_valid():
    #         print("valid")
    #         # word = form.save(commit=False)
    #         word = form.save()
    #         # word.word = "asdsad"
    #         # word.description = request.description
    #         # post.author = request.user
    #         # word.published_date = timezone.now()
    #         word.save()
    #     else:
    #         print("Not valid")
    # else:
    #     form = PublishWordForm()
    #     # print(request.word)
    # return render(request, 'publish/publish_edit.html', {'form': form})