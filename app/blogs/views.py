from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post

# Prevent others to update/delete since
# @decoraters doesn't work in generic views
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Same can be done using generic views [PostlistView]
"""
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', context)
"""


class PostsListView(ListView):
    model = Post
    # Default lookup is <app>/<model>_<viewtype>.html
    # Default: blogs/post_list.html
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # Paginator is impoted default -> Set # posts per page
    paginate_by = 5


class UserPostsListView(ListView):
    model = Post
    # Default: blogs/post_list.html
    template_name = 'blogs/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted'] #Gets overwritten below
    # Paginator is impoted default -> Set # posts per page
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostsDetailView(DetailView):
    model = Post


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # Default view: blogs/post_form.html
    template_name = 'blogs/create_post.html'

    # It doesn't recognize author so have to add it
    def form_valid(self, form):
        form.instance.author = self.request.user
        # redirect to the created post (resource) using get_absolute_url() in models
        return super().form_valid(form)


class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # Default view: blogs/post_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # [Security] Check if the author is making the modifications
    # test_func() is from django.contrib.auth.mixins.UserPassesTestMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # Default view: blogs/post_confirm_delete.html

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blogs/about.html')
