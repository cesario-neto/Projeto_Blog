from django.views.generic import ListView
from post.models import Post


class PostsListView(ListView):
    queryset = Post.objects.filter(is_publishe=True)
    context_object_name = 'posts'
    template_name = 'post/pages/home.html'
    paginate_by = 9
