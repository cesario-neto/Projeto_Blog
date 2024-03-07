from django.urls import path
from .views import PostsListView, PostDetailView, SearchPostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('search/', SearchPostsListView.as_view(), name='search')
]
