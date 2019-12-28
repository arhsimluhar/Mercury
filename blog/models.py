from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))
    POST_CHOICES = (("markdown", "Markdown"), ("HTML", "html"))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, related_name="blog_posts", default="admin"
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    postType = models.CharField(max_length=10, choices=POST_CHOICES, default="markdown")

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail_by_date_slug",
            args=[
                self.publish.year,
                self.publish.strftime("%b"),
                self.publish.day,
                self.slug,
            ],
        )

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # To manaully deactivate inappropriate comments
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=140)
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return self.subject
