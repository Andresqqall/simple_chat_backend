from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

from apps.users.managers import ExtendedUserManager


class User(AbstractUser):
    """
        Extended AbstractUser
    """
    objects = ExtendedUserManager()

    def __str__(self):
        return f"User ({self.id}) Email: ({self.email})"
