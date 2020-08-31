from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #user can update only its own post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

#using class baase views insted of function views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #cruntly it is looking for list and we tell it to look as post
    ordering = ['-date_posted'] #ordering newest to older
    paginate_by = 5  #don't need to import

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #cruntly it is looking for list and we tell it to look as post
    #ordering = ['-date_posted'] #ordering newest to older
    paginate_by = 5  #don't need to import

    def get_queryset(self): #override function
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(auther=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overriding function to tell current user is auther
        form.instance.auther = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overriding function to tell current user is auther
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):#user can update only its own post
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):#user can delete only its own post
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
