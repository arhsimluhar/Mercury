from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


class LoginUser(auth_views.LoginView):
    template_name = "mercury/login.html"
    next = ""


class LogoutUser(auth_views.LogoutView):
    template_name = "mercury/base.html"


class homepage(TemplateView):
    template_name = "blog/base.html"
