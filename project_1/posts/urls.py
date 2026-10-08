from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts_list', views.posts_list),
    path('group_posts/<slug:slug>/', views.group_posts),
]
