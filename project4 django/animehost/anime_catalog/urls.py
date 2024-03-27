from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_catalog, name='anime_catalog'),
]
