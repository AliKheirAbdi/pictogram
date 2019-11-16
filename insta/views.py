from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
)
from datetime import datetime
from .models import Post

# Create your views here.


class PostListView(ListView):
    template_name = "insta/home.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostCreateView(CreateView):
    template_name = 'insta/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    #to send users back to homepage after creating a post
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = 'insta/post_detail.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)