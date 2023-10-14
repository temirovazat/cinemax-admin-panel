# Generated by Django 3.2 on 2022-11-07 09:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid
from typing import List


class Migration(migrations.Migration):

    initial = True

    dependencies: List = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('creation_date', models.DateField(db_index=True, null=True, verbose_name='creation date')),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating')),
                ('type', models.CharField(choices=[('movie', 'movie'), ('tv show', 'tv show')], max_length=255, verbose_name='type')),
            ],
            options={
                'verbose_name': 'film work',
                'verbose_name_plural': 'film works',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('actor', 'actor'), ('director', 'director'), ('writer', 'writer')], max_length=255, verbose_name='role')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personfilmwork', to='movies.filmwork')),
                ('related_obj', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person')),
            ],
            options={
                'verbose_name': 'person film work',
                'verbose_name_plural': 'persons film work',
                'db_table': 'content"."person_film_work',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genrefilmwork', to='movies.filmwork')),
                ('related_obj', models.ForeignKey(db_column='genre_id', on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre')),
            ],
            options={
                'verbose_name': 'genre film work',
                'verbose_name_plural': 'genres film work',
                'db_table': 'content"."genre_film_work',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(related_name='film_works', through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(related_name='film_works', through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['film_work', 'related_obj'], name='movies_personfilmwork_idx'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'related_obj', 'role'), name='unique_movies_personfilmwork'),
        ),
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['film_work', 'related_obj'], name='movies_genrefilmwork_idx'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'related_obj'), name='unique_movies_genrefilmwork'),
        ),
    ]
