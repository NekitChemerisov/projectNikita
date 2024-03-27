from django.contrib import admin
from .models import Anime

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'video_url')

admin.site.register(Anime, AnimeAdmin)
