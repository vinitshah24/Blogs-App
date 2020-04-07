from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import (
    PostsListView,
    UserPostsListView,
    PostsDetailView,
    PostsCreateView,
    PostsUpdateView,
    PostsDeleteView
)

urlpatterns = [
    # Same Functionality achieved using PostListView
    # path('', views.home, name='blogs-home'),
    path('', PostsListView.as_view(), name='blogs-home'),
    path('post/<int:pk>/', PostsDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostsListView.as_view(), name='user-posts'),
    path('post/new/', PostsCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostsUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostsDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blogs-about'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
