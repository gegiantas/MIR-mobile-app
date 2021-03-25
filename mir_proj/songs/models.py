from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField("Title", max_length=240)
    album = models.CharField("Album",max_length=240)
    artist = models.CharField("Artist",max_length=100)
    released_date = models.DateField("Released Date", null=True, blank=True,default=None)
    spotify_id = models.CharField("Spotify Id",null=True, blank=True,default=None,max_length=100)

    energy_low = models.DecimalField ("Energy_Low",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    energy_med = models.DecimalField ("Energy_Medium",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    energy_high = models.DecimalField ("Energy_High",max_digits=10, decimal_places=4, null=True, blank=True,default=None)

    valence_low = models.DecimalField ("Valence_Low",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    valence_med = models.DecimalField ("Valence_Medium",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    valence_high = models.DecimalField ("Valence_High",max_digits=10, decimal_places=4, null=True, blank=True,default=None)

    danceability_low = models.DecimalField ("Danceability_Low",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    danceability_med = models.DecimalField ("Danceability_Medium",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    danceability_high = models.DecimalField ("Danceability_High",max_digits=10, decimal_places=4, null=True, blank=True,default=None)

    speechiness_low = models.DecimalField ("Speechiness_Low",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    speechiness_med = models.DecimalField ("Speechiness_Medium",max_digits=10, decimal_places=4, null=True, blank=True,default=None)
    speechiness_high = models.DecimalField ("Speechiness_High",max_digits=10, decimal_places=4, null=True, blank=True,default=None)

    def __str__(self):
        return self.title


class Segment(models.Model):
    title = models.CharField("Title", max_length=240)
    segment = models.FileField(upload_to='music_segments/')



    def __str__(self):
        return self.title
