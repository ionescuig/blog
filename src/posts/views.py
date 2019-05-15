from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post


class HomeView(TemplateView):
    template_name = 'posts/index.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    form_class = PostForm
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        return context

    def get_queryset(self):
        return Post.objects.all()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'posts/post_update.html'
    form_class = PostForm

    def get_queryset(self):
        return Post.objects.all()


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'posts/post_delete.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:list')

    def get_queryset(self):
        return Post.objects.all()


class PostListView(ListView):
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return Post.objects.all().order_by("-published_date")
