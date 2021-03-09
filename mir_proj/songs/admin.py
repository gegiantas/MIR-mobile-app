from django.contrib import admin

from .models import Song

class SongAdmin(admin.ModelAdmin):
  list = ('name', 'album', 'artist','released_date','energy_low,energy_med','energy_high','valence_low','valence_med','valence_high','danceability_low','danceability_med','danceability_high')

admin.site.register(Song, SongAdmin)

# Register your models here.
