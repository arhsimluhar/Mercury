# https://​docs.​djangoproject.​com/​en/​2.​0/​topics/​http/​urls/​#path-​converters.
# https:/​/​docs.​djangoproject.​com/​en/2.​0/​ref/​urls/​#django.​urls.​re_​path

# application namespace
from django.urls import path

from . import views

app_name = "seeker"
urlpatterns = [
    path("", views.HomePage.as_view(), name="home")
]
