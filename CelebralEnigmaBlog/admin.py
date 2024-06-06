from django.contrib import admin
from .models import Post,Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.site_header = 'Celebral Enigma'
admin.site.site_title = 'Celebral Enigma'
admin.site.index_title = 'Welcome to Your Site Admin'