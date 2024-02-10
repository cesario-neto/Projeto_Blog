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