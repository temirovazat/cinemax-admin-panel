from typing import Any, Dict

from django.contrib.postgres.aggregates import ArrayAgg
from django.db import models
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import Filmwork, Role


class MoviesApiMixin:
    """Base class for film representation."""

    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self) -> QuerySet[Filmwork]:
        """Prepare a query with all films.

        - Order by creation date;
        - Represented as dictionaries;
        - Add genres and roles of film participants.

        Returns:
            QuerySet[Filmwork]: Films as dictionaries.
        """
        genres = {
            'genres': ArrayAgg(
                'genres__name',
                distinct=True,
                filter=models.Q(genrefilmwork__related_obj__name__isnull=False),
            ),
        }
        persons = {
            f'{role}s': ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=models.Q(personfilmwork__role=role),
            )
            for role, _ in Role.choices
        }
        return (
            Filmwork.objects
            .order_by('created')
            .values('id', 'title', 'description', 'creation_date', 'rating', 'type')
            .annotate(**genres, **persons)
        )

    def render_to_response(self, context: Dict[str, Any], **kwargs: Any) -> JsonResponse:
        """Format the film page data into JSON.

        Args:
            context: Film page dictionary;
            kwargs: Optional named arguments.

        Returns:
            JsonResponse: Film page in JSON.
        """
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    """Class for displaying all films."""

    paginate_by = 50

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dictionary with data for creating a film page.

        Args:
            kwargs: Optional named arguments.

        Returns:
            dict[str, any]: Dictionary for paginated film display.
        """
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by,
        )
        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    """Class for displaying a single film."""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dictionary with data for creating a single film page.

        Args:
            kwargs: Optional named arguments.

        Returns:
            dict[str, any]: Dictionary for displaying a film.
        """
        context = super().get_context_data()
        return context['object']
