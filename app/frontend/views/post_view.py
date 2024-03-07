from django.views.generic import ListView, DetailView
from post.models import Post


def make_range_page(page_range, current_page):

    start_page = current_page - 2
    stop_page = current_page + 2

    total_pages = len(page_range)

    if start_page < 1:
        stop_page += abs(start_page)
        start_page = 0

    if stop_page >= total_pages:
        start_page -= abs(stop_page - total_pages)
        stop_page = total_pages

    page_range = page_range[start_page:stop_page]

    return page_range


class PostsListView(ListView):
    queryset = Post.objects.filter(is_publishe=True)
    context_object_name = 'posts'
    template_name = 'post/pages/home.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        paginator = ctx.get('paginator')
        page_obj = ctx.get('page_obj')

        page_range = make_range_page(
            paginator.page_range, page_obj.number)

        ctx.update({
            'page_range': page_range,
        })
        return ctx


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
        paginator = ctx.get('paginator')
        page_obj = ctx.get('page_obj')

        page_range = make_range_page(
            paginator.page_range, page_obj.number)

        print(page_range)

        query = self.request.GET.get('q', '')
        query_term = f'&q={query}'

        ctx.update({
            'query': query,
            'query_term': query_term,
            'page_range': page_range,
        })

        return ctx
