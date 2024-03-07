from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from post.models import Post


class PostsListView(ListView):
    queryset = Post.objects.filter(is_publishe=True)
    context_object_name = 'posts'
    template_name = 'post/pages/home.html'
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_publishe=True).select_related('category')
    context_object_name = 'post'
    template_name = 'post/pages/post.html'
    slug_field = 'slug'


class SearchPostsListView(ListView):
    queryset = Post.objects.filter(is_publishe=True)
    context_object_name = 'posts'
    template_name = 'post/pages/home.html'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        qs = super().get_queryset()

        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        ctx.update({'query': query})
        return ctx
