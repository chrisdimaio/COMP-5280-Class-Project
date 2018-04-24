from django.shortcuts import render, redirect
from .forms import PublishWordForm
from django.views.generic import TemplateView
from publish.models import Post
from django.utils import timezone

class HomeView(TemplateView):
    template_name = 'publish/home.html'

    def get(self, request, *args, **kwargs):
        words = Post.objects.all().order_by('-id')
        return render(request, self.template_name, {'words': words})

    def Post(self, request):
        words = Post.objects.all().order_by('-id')
        return render(request, self.template_name, {'words': words})


class PublishView(TemplateView):
    template_home = 'publish/home.html'
    template_name = 'publish/publish_edit.html'

    def get(self, request, *args, **kwargs):
        form = PublishWordForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PublishWordForm(request.POST)
        if form.is_valid():
            form.save()
            # form = PublishWordForm()
            return redirect('home')
        return render(request, self.template_name, {'form': form})