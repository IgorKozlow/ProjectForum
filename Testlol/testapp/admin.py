from django.contrib import admin
from .models import *


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['author','title', 'content', 'photo', 'time_create', 'time_updated', 'is_published']
    fields = ['author', 'title', 'content', 'photo', 'cat']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'user_comment', 'create_date', 'status' ]
    fields = ['author', 'post', 'user_comment', 'status' ]