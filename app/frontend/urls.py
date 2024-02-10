from django.urls import path
from .views import PostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('/post/<slug:slug>', PostsListView.as_view(), name='post'),
]
