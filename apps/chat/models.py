from django.contrib.auth import get_user_model
from django.db import models

from apps.chat.managers import ThreadManager, MessageManager
from apps_generic.whodidit.models import WhoDidIt

User = get_user_model()


class Thread(WhoDidIt):
    """
        Represents a chat thread.

        Attributes:
            participants (ManyToManyField): A many-to-many relationship to the User model, representing
                                            the chat members involved in this thread.
    """
    objects = ThreadManager()

    participants = models.ManyToManyField(
        to=User,
        verbose_name='chat members',
        related_name='participants'
    )

    class Meta:
        ordering = ['-id']


class Message(WhoDidIt):
    """
       Represents a message in a chat thread.

       Attributes:
           thread (ForeignKey): A foreign key to the Thread model, representing the thread to which the message belongs.
                               The message will not be deleted if the thread is deleted, but the foreign key
                               will be set to NULL instead.
           text (TextField): The content of the message.
           is_read (BooleanField): Indicates whether the message has been read. Defaults to False.
    """
    objects = MessageManager()

    thread = models.ForeignKey(
        to=Thread,
        verbose_name='message tread',
        related_name='tread_messages',

        # This can also be CASCADE, but I think it's better to store the message to avoid other causes.
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.TextField(
        verbose_name='message text'
    )
    is_read = models.BooleanField(
        verbose_name='is message read',
        default=False
    )

    class Meta:
        ordering = ['-id']
