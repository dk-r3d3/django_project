from django.shortcuts import render
from django.http import HttpResponse

"""
views.py — тут хранятся обработчики запросов (функции или классы, получающие запрос и генерирующие ответ).
Документация.https://docs.djangoproject.com/en/2.2/topics/http/views/
 """


# Create your views here.


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def posts_list(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug): # если pk, то pk
    return HttpResponse(f'Пост номер {slug}')
