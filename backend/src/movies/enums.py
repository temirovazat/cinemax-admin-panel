from django.db import models
from django.utils.translation import gettext_lazy as _


class Type(models.TextChoices):
    """Helper model for choosing types of film works."""

    movie = 'movie', _('movie')
    tv_show = 'tv show', _('tv show')


class Role(models.TextChoices):
    """Helper model for choosing roles of individuals."""

    actor = 'actor', _('actor')
    director = 'director', _('director')
    writer = 'writer', _('writer')
