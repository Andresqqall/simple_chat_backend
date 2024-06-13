from django.db import models

from infrastructure.middlewares.current_request import current_request


class ThreadManager(models.Manager):

    def with_default_filters(self):
        """
            Apply default filters to a queryset.

            Returns:
                QuerySet: A queryset filtered by the default criteria.
        """
        request = current_request()
        user = request.user
        return self.filter(
            participants=user
        )


class MessageManager(models.Manager):

    def with_default_filters(self):
        """
            Apply default filters to a queryset.

            Returns:
                QuerySet: A queryset filtered by the default criteria.
        """
        request = current_request()
        user = request.user
        return self.filter(
            tread__participants=user
        )
