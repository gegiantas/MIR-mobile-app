# Generated by Django 3.1.7 on 2021-03-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20210309_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='danceability_high',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Danceability_High'),
        ),
        migrations.AlterField(
            model_name='song',
            name='danceability_low',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Danceability_Low'),
        ),
        migrations.AlterField(
            model_name='song',
            name='danceability_med',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Danceability_Medium'),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy_high',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='Energy_High'),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy_low',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Energy_Low'),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy_med',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Energy_Medium'),
        ),
        migrations.AlterField(
            model_name='song',
            name='released_date',
            field=models.DateField(blank=True, null=True, verbose_name='Released Date'),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness_high',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Speechiness_High'),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness_low',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Speechiness_Low'),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness_med',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Speechiness_Medium'),
        ),
        migrations.AlterField(
            model_name='song',
            name='valence_high',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Valence_High'),
        ),
        migrations.AlterField(
            model_name='song',
            name='valence_low',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Valence_Low'),
        ),
        migrations.AlterField(
            model_name='song',
            name='valence_med',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Valence_Medium'),
        ),
    ]
