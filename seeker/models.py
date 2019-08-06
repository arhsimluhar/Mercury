# Create your models here.
from django.db import models


class Solution(models.Model):
    supported_languages = (("python2", "Python 2"), ("python3", "Python 3"), ("c++", "C++ 17"))
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=10, choices=supported_languages, default="c++")
    code = models.TextField(max_length=4096, )

    testcases = models.ForeignKey

    class Meta:
        ordering = ('-created',)


class Testcases(models.Model):
    created = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Solution,
                             on_delete=models.CASCADE,
                             related_name='testcases')
    updated = models.DateTimeField(auto_now=True)
