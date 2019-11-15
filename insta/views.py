from django.shortcuts import render
from .models import Post
from django.views.generic import(
    ListView
)

# Create your views here.


class PostListView(ListView):
    template_name = "insta/home.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
