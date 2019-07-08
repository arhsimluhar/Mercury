from django.urls import path

from . import views

# https://​docs.​djangoproject.​com/​en/​2.​0/​topics/​http/​urls/​#path-​converters.
# https:/​/​docs.​djangoproject.​com/​en/2.​0/​ref/​urls/​#django.​urls.​re_​path

# application namespace
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]
