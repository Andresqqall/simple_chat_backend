from django.contrib.auth import get_user_model
from drf_rw_serializers import generics
from rest_framework.generics import get_object_or_404

from apps.users.serializers import BaseUserSerializer

User = get_user_model()


class UserSelfAPIView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve and update information for the authenticated user.
    """
    serializer_class = BaseUserSerializer

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)
