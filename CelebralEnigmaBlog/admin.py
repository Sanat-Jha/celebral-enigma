from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Post,Category,EmailSubs
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(EmailSubs)
# Unregister the User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Celebral Enigma'
admin.site.site_title = 'Celebral Enigma'
admin.site.index_title = 'Welcome to Your Site Admin'