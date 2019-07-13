from django.contrib.auth import views as auth_views
from django.shortcuts import render


class LoginUser(auth_views.LoginView):
    template_name = "mercury/login.html"
    next = ""


class LogoutUser(auth_views.LogoutView):
    pass

def homepage(request):
    return render(request, "blog/base.html")

