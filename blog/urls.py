from django.urls import path
from . import views
from .views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout", views.logout_request, name= "logout"),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('post_comment/<int:pk>/', views.comment_view, name='post_comment'),
]