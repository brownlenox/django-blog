from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . models import Article
from django.urls import reverse_lazy
from . forms import BlogPostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin, ListView):
    model = Article
    redirect_field_name = 'next'
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

class CreateBlog( LoginRequiredMixin,  CreateView):
    model=Article
    form_class=BlogPostForm
    template_name="blog/new_blog.html"
    success_url=reverse_lazy("index")

    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super().form_valid(form_class)
        
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('detail_article', kwargs={'pk': pk})

    # def dispatch(self, request, *args, **kwargs):
    #     post = self.get_object()
    #     if request.user != post.author:
    #         return HttpResponseForbidden() 
    #     return super().dispatch(request, *args, **kwargs)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('index')

    # def dispatch(self, request, *args, **kwargs):
    #     post = self.get_object()
    #     if request.user != post.author:
    #         return HttpResponseForbidden()
    #     return super().dispatch(request, *args, **kwargs)