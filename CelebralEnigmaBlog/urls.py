from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<str:title>", views.post, name="post"),
    path("category/<str:cat>", views.category, name="post"),
    path("write/sanatJha", views.write, name="write"),
    path("addpost", views.addpost, name="addpost"),
]
