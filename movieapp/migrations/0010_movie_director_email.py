# Generated by Django 5.0 on 2024-01-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0009_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='Sugardady@ya.ru', max_length=254),
        ),
    ]
