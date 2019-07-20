import os

from faker import Faker

os.chdir("../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mercury.settings")
import django

django.setup()
from django.contrib.auth.models import User
from django.utils.text import slugify
from blog import models

PostNum = 20

fake = Faker()
user = User.objects.get(username="rahul")
for i in range(PostNum):
    title = fake.name_male()
    post = models.Post(
        title=title,
        author=user,
        body=fake.text(),
        slug=slugify(title),
        status="published",
    )
    post.save()
