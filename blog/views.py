from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (ListView,
                                   DetailView,
                                   CreateView,
                                   UpdateView,
                                    DeleteView)
from django.http import HttpResponse

context = {
        'posts': Post.objects.all(),
        'title': 'this is blog post'
    }

def home(request):

    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'blog post'})

class PostListView(LoginRequiredMixin, ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # we can order with the date_posted

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class CreateDetailPost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateDetailPost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

class DeletePost(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Post
    success_url='/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False








