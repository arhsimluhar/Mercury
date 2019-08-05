# Create your models here.
from django.db import models


class Solution(models.Model):
    supported_languages = (("python2", "Python 2"), ("python3", "Python 3"), ("c++", "C++ 17"))
    created = models.DateField(auto_now_add=True)

    language = models.CharField(max_length=10, choices=supported_languages, default="c++")

    class Meta:
        ordering = ('-created',)
