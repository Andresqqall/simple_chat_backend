from django.apps import apps
from django.contrib.auth.models import UserManager
from django.db import models
from django.db.models import Subquery, OuterRef, Count


class ExtendedUserManager(UserManager):
    """
    Custom user manager that extends the default UserManager to include additional annotations.
    """

    def get_queryset(self):
        """
        Overrides the default queryset to include an annotation for unread message count.
        """
        return super().get_queryset().annotate(
            unread_message_count=self.unread_message_count(),
        )

    @staticmethod
    def unread_message_count() -> Subquery:
        """
        Creates a Subquery that calculates the number of unread messages for each user.
        """
        message = apps.get_model('chat', 'Message')

        unread_messages = message.objects.only('id').filter(
            thread__participants__id=OuterRef('pk'),
            is_read=False
        ).exclude(
            created_by__pk=OuterRef('pk')
        ).values(
            'created_by'
        ).annotate(
            unread_count=Count('id', distinct=True)
        ).order_by(
            '-unread_count'
        ).values(
            'unread_count'
        )[:1]
        return Subquery(unread_messages, output_field=models.IntegerField())
