from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)} # autocomplete slug
    save_on_top = True # duplicate save button on top

admin.site.register(Post, PostAdmin)
