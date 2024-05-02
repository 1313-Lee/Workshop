from django.urls import path
from .views import *

urlpatterns = [
    path("album/<int:pk>/delete/", AlbumDeleteView.as_view(), name="album_delete"),
    path("album/<int:pk>/edit/", AlbumUpdateView.as_view(), name="album_edit"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("album/new/", AlbumCreateView.as_view(), name="album_new"),
    path("album", AlbumListView.as_view(), name="album"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/new/", BlogCreateView.as_view(), name="blog_new"),
    path("blog", BlogListView.as_view(), name="blog"),
    path("topic", TopicListView.as_view(), name="topic"),
    path("", HomeListView.as_view(), name="home"),
]

