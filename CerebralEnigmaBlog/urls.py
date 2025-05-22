from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, CategorySitemap

sitemaps = {
    'posts': PostSitemap,
    'categories': CategorySitemap,
}


urlpatterns = [
    path("", views.home, name="home"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("post/<str:title>", views.post, name="post"),
    path("category/<str:cat>", views.category, name="category"),
    path("write/", views.write, name="write"),
    path("addpost", views.addpost, name="addpost"),
    path('increaseviewcount/', views.increase_view_count, name='increase_view_count'),
    path('newsubscribe', views.newsubscribe, name='newsubscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('valid_write_password', views.valid_write_password, name='valid_write_password'),
]

