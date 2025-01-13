from django.db import models
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    description = models.TextField(default=" ",max_length=600)
    content = models.TextField(default=" ")
    date = models.DateField(default=date.today)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField('Post', related_name='categories')
    def __str__(self):
        return self.name
    def get_post_titles(self):
        return self.posts.values_list('title', flat=True)
    
class EmailSubs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self) -> str:
        return self.name