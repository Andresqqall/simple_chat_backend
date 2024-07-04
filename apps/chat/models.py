from django.contrib.auth import get_user_model
from django.db import models

from apps.chat.managers import ThreadManager, MessageManager
from apps_generic.whodidit.models import WhoDidIt

User = get_user_model()


class Thread(WhoDidIt):
    """
    Represents a chat thread.
    """
    objects = ThreadManager()

    participants = models.ManyToManyField(
        to=User,
        verbose_name='chat members',
        related_name='participants'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Thread ({self.id})"


class Message(WhoDidIt):
    """
    Represents a message in a chat thread.
    """
    objects = MessageManager()

    thread = models.ForeignKey(
        to=Thread,
        verbose_name='message thread',
        related_name='thread_messages',
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

    def __str__(self):
        return f"Message ({self.id}) in Thread ({self.thread.id})"
