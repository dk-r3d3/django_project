from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком мороженого
    path('first_app_ice/', views.ice_cream_list),
    # Страница с информацией об одном сорте мороженого;
    # в качестве параметра ожидает целое положительное число или 0
    path('first_app_ice/<int:pk>/', views.ice_cream_detail),
]