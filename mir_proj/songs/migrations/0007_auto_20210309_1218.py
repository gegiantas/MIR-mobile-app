# Generated by Django 3.1.7 on 2021-03-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_song_spotify_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='spotify_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Spotify Id'),
        ),
    ]