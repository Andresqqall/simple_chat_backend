from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

"""
    User serializers:
"""


class BaseUserSerializer(serializers.ModelSerializer):
    """
    Base representation of user serializer
    """

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'unread_message_count'
        ]

    first_name = serializers.CharField(min_length=5, max_length=150)
    last_name = serializers.CharField(min_length=5, max_length=150)
    unread_message_count = serializers.IntegerField(default=0, read_only=True)
