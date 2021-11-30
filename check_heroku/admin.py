from django.contrib import admin

from .models import *


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'slug', 'content')
#     fields = ('title', 'slug', 'content', 'created_at', )

# admin.site.register(Post, PostAdmin)
admin.site.register(Post)
