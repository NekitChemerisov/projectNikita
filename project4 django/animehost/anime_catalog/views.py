from django.shortcuts import render
from .models import Anime

def anime_catalog(request):
    animes = Anime.objects.all()
    return render(request, 'anime_catalog/catalog.html', {'animes': animes})
