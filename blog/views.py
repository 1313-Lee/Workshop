from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Topic, Image

# Create your views here.
class HomeListView(ListView):
    model = Post
    template_name = "home.html"

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ["title", "topic", "body", "image",]

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields = ["title", "topic", "body", "image",]

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog")

class TopicListView(ListView):
    model = Topic
    template_name = "topic.html"

class AlbumListView(ListView):
    model = Image
    template_name = "album.html"

class AlbumCreateView(CreateView):
    model = Image
    template_name = "album_new.html"
    fields = ["title", "image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8", "image9"]

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class AlbumDetailView(DetailView):
    model = Image
    template_name = "album_detail.html"

class AlbumUpdateView(UpdateView):
    model = Image
    template_name = "album_edit.html"
    fields = ["title", "image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8", "image9"]

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class AlbumDeleteView(DeleteView):
    model = Image
    template_name = "album_delete.html"
    success_url = reverse_lazy("album")

