from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name='blog_posts', default="admin")
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail_by_date_slug',
                       args=[self.publish.year,
                             self.publish.strftime('%b'),
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
