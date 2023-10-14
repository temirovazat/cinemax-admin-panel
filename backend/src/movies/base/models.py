import uuid

from django.db import models


class TimeStampedMixin(models.Model):
    """Abstract model for timestamp tracking."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadata."""

        abstract = True


class UUIDMixin(models.Model):
    """Abstract model for generating primary keys as UUIDs."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Metadata."""

        abstract = True


class FilmworkM2M(UUIDMixin, TimeStampedMixin):
    """Abstract model for relationships between film works and other objects."""

    film_work = models.ForeignKey(
        'movies.Filmwork',
        on_delete=models.CASCADE,
        related_name='%(class)s',
    )
    modified = None

    class Meta:
        """Metadata."""

        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'related_obj'],
                name='unique_%(app_label)s_%(class)s',
            ),
        ]
        indexes = [
            models.Index(
                fields=['film_work', 'related_obj'],
                name='%(app_label)s_%(class)s_idx',
            ),
        ]
