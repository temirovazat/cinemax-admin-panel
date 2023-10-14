from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.base.models import FilmworkM2M, TimeStampedMixin, UUIDMixin
from movies.enums import Role, Type

DEFAULT_LENGTH = 255


class Person(UUIDMixin, TimeStampedMixin):
    """Base model for individuals."""

    full_name = models.CharField(_('full name'), max_length=DEFAULT_LENGTH)

    class Meta:
        """Metadata for individuals."""

        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self) -> str:
        """Return the full name of a person as a string.

        Returns:
            str: Full name of the person
        """
        return self.full_name


class Genre(UUIDMixin, TimeStampedMixin):
    """Base model for genres."""

    name = models.CharField(_('name'), max_length=DEFAULT_LENGTH)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        """Metadata for genres."""

        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    def __str__(self):
        """Return the name of the genre as a string.

        Returns:
            str: Name of the genre
        """
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    """Base model for filmworks."""

    title = models.CharField(_('title'), max_length=DEFAULT_LENGTH)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(
        _('creation date'),
        null=True,
        db_index=True,
    )
    rating = models.FloatField(
        _('rating'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.CharField(
        _('type'),
        max_length=DEFAULT_LENGTH,
        choices=Type.choices,
    )
    genres = models.ManyToManyField(
        Genre,
        through='GenreFilmwork',
        related_name='film_works',
    )
    persons = models.ManyToManyField(
        Person,
        through='PersonFilmwork',
        related_name='film_works',
    )

    class Meta:
        """Metadata for filmworks."""

        db_table = "content\".\"film_work"
        verbose_name = _('film work')
        verbose_name_plural = _('film works')

    def __str__(self):
        """Return the title of the filmwork as a string.

        Returns:
            str: Title of the filmwork
        """
        return self.title


class GenreFilmwork(FilmworkM2M):
    """Intermediate model for filmworks and genres."""

    related_obj = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        db_column='genre_id',
        verbose_name=_('genre'),
    )

    class Meta(FilmworkM2M.Meta):
        """Metadata for genres in filmworks."""

        db_table = "content\".\"genre_film_work"
        verbose_name = _('genre film work')
        verbose_name_plural = _('genres film work')


class PersonFilmwork(FilmworkM2M):
    """Intermediate model for filmworks and individuals."""

    related_obj = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id',
        verbose_name=_('person'),
    )
    role = models.CharField(
        _('role'),
        max_length=DEFAULT_LENGTH,
        choices=Role.choices,
    )

    class Meta(FilmworkM2M.Meta):
        """Metadata for individuals in filmworks."""

        db_table = "content\".\"person_film_work"
        verbose_name = _('person film work')
        verbose_name_plural = _('persons film work')
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'related_obj', 'role'],
                name='unique_%(app_label)s_%(class)s',
            ),
        ]
