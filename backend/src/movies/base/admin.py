from django.contrib import admin

from movies.models import GenreFilmwork, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    """Class for inserting genres into the movie admin interface."""

    model = GenreFilmwork
    autocomplete_fields = ('related_obj',)


class PersonFilmworkInline(admin.TabularInline):
    """Class for inserting people into the movie admin interface."""

    model = PersonFilmwork
    autocomplete_fields = ('related_obj',)
