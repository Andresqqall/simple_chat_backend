from django.apps import apps
from django.contrib.auth.models import UserManager
from django.db import models
from django.db.models import Subquery, OuterRef, Count, F, Q


class ExtendedUserManager(UserManager):
    """
    Custom user manager that extends the default UserManager to include additional annotations.
    """

    def get_queryset(self):
        """
        Overrides the default queryset to include an annotation for unread message count.

        Returns:
            QuerySet: The queryset annotated with unread message counts.
        """
        return super().get_queryset().annotate(
            unread_message_count=self.unread_message_count(),
        )

    @staticmethod
    def unread_message_count() -> Subquery:
        """
        Creates a Subquery that calculates the number of unread messages for each user.

        The subquery filters messages where the user is a participant and the message is unread,
        but excludes messages created by the user themselves. It then counts the distinct message IDs.

        Returns:
            Subquery: A Django Subquery object that can be used in annotations.
        """
        message = apps.get_model('chat', 'Message')
        return Subquery(
            message.objects.only('id').filter(
                Q(thread__participants__id=OuterRef('pk')) & Q(is_read=False) & ~Q(created_by__pk=OuterRef('pk'))
            ).values('created_by').annotate(
                unread_count=Count('id', distinct=True)
            ).order_by('-unread_count').values('unread_count')[:1],
            output_field=models.IntegerField()
        )
