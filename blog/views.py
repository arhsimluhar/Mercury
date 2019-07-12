# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
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




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
