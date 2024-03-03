from django.urls import path
from .views import PostsListView, PostDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post'),
]
