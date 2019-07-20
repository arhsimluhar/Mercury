# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from taggit.models import Tag

from .models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    ordering = ["publish"]

    def get_queryset(self):
        if 'tag_slug' in self.kwargs:
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            return Post.objects.all().filter(tags__in=[tag])
        else:
            return Post.objects.all()


class PostDateDetailView(DateDetailView):
    date_field = 'publish'
    template_name = 'blog/post/detail.html'
    queryset = Post.objects.all().filter(status='published')


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", 'slug', 'author', 'body', 'status']
    template_name = 'blog/post/update.html'


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ["title", 'slug', 'author', 'body', 'status']
    template_name = 'blog/post/update.html'
