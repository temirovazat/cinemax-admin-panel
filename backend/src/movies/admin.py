from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from movies.base.admin import GenreFilmworkInline, PersonFilmworkInline
from movies.models import Filmwork, Genre, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin class for persons."""

    list_display = ('full_name', 'get_roles')
    list_filter = ('personfilmwork__role',)
    search_fields = ('full_name', 'id')

    @admin.display(description=_('role'))
    def get_roles(self, obj: Person) -> str:
        """Display person's roles.

        Args:
            obj: Person

        Returns:
            str: Role names
        """
        return ', '.join(
            {str(_(obj.role)) for obj in obj.personfilmwork_set.all()},
        )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin class for genres."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description', 'id')


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    """Admin class for filmworks."""

    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    list_display = (
        'title',
        'creation_date',
        'rating',
        'get_genres',
        'get_persons',
    )
    list_filter = ('type', 'genres')
    search_fields = ('title', 'description', 'id', 'persons__full_name')
    list_prefetch_related = ('genres', 'persons')

    def get_queryset(self, request: HttpRequest) -> QuerySet[Filmwork]:
        """Load filmworks and prefetch related data.

        Args:
            request: Request

        Returns:
            QuerySet[Filmwork]: Filmworks with genres and persons
        """
        return super().get_queryset(
            request,
        ).prefetch_related(
            *self.list_prefetch_related,
        )

    @admin.display(description=_('genres'))
    def get_genres(self, obj: Filmwork) -> str:
        """Display filmwork's genre names.

        Args:
            obj: Filmwork

        Returns:
            str: Genre names
        """
        return ','.join([genre.name for genre in obj.genres.all()])

    @admin.display(description=_('persons'))
    def get_persons(self, obj: Filmwork) -> str:
        """Display names of filmwork's contributors.

        Args:
            obj: Filmwork

        Returns:
            str: Person names
        """
        return ','.join([person.full_name for person in obj.persons.all()])
