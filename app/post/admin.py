from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content',
    list_display = 'title', 'category', 'author'
    list_filter = 'category__name', 'is_publishe'
    search_fields = 'title', 'author__username',
