# Generated by Django 3.1.7 on 2021-03-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20210309_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='spotify_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Spotify Id'),
        ),
    ]