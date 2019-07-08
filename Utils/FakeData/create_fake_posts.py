import sys

from django.contrib.auth.models import User
from faker import Faker

sys.path.append("../../blog")
from blog import models

PostNum = 100

fake = Faker()
user = User.objects.get(username='rahul')
for i in range(PostNum):
    print("coming here")
    post = models.Post(title=fake.name_male(), author=user, body=fake.text())
    post.save()
