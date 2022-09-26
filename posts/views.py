from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'posts/home.html'

class AboutPageView(TemplateView):
    template_name = 'posts/about.html'

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

    class PostCreateView(CreateView):
        template_name = "posts/new.html"
        model = Post
        fields = title subtitile, author, posts