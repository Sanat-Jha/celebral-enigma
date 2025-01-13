from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<str:title>", views.post, name="post"),
    path("category/<str:cat>", views.category, name="post"),
    path("write/", views.write, name="write"),
    path("addpost", views.addpost, name="addpost"),
    path('increaseviewcount/', views.increase_view_count, name='increase_view_count'),
    path('newsubscribe', views.newsubscribe, name='newsubscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
]

