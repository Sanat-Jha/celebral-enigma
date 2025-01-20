from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return reverse('post', kwargs={'title': obj.title})


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('category', kwargs={'cat': obj.name})
