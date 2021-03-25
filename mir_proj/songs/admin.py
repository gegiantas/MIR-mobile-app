from django.contrib import admin

from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  list_filter = ('title', 'album', 'artist','released_date')
  list_display = ('title', 'album', 'artist','released_date')

#admin.site.register(Song, SongAdmin)

# Register your models here.
