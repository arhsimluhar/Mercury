from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "seeker/home.html"

    def post(self):
        pass
