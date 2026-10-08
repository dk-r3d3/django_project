from django.apps import AppConfig

"""
apps.py — настройки конфигурации приложения. 
Документация. https://docs.djangoproject.com/en/2.2/ref/applications/#configuring-applications
"""


class FirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_app_ice'
