# Generated by Django 4.2.2 on 2023-06-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movieorder'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='movies',
            field=models.ManyToManyField(related_name='users', through='movies.MovieOrder', to='movies.movie'),
        ),
    ]