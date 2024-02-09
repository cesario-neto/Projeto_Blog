from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'category', 'author'
    list_filter = 'category__name', 'is_publishe'
    search_fields = 'title', 'author__username',
