from rest_framework import serializers

from apps.chat.models import Thread, Message
from apps.users.serializers import BaseUserSerializer
from apps_generic.whodidit.serializers import BaseWhoDidItSerializer

"""
    Tread Serializers: 
"""


class BaseThreadSerializer(serializers.ModelSerializer):
    """
        Base Thread Serializer.
    """

    class Meta:
        model = Thread
        fields = BaseWhoDidItSerializer.Meta.fields + [
            'participants'
        ]
        read_only_fields = BaseWhoDidItSerializer.Meta.read_only_fields


class DetailThreadSerializer(BaseThreadSerializer):
    """
        Detail Thread Serializer only for read operations.
    """
    participants = BaseUserSerializer(many=True)


class CreateTreadSerializer(BaseThreadSerializer):
    """
        Create Thread Serializer only for create operations.
    """

    @staticmethod
    def validate_participants(participants):
        """
        Validates that the participants list does not contain more than 2 participants.

        Args:
            participants (list): List of participants to validate.

        Returns:
            list: The validated participants list if valid.

        Raises:
            serializers.ValidationError: If participants list contains more than 2 participants.
        """
        if len(participants) > 2:
            raise serializers.ValidationError("Participants list cannot have more than 2 participants.")
        return participants


"""
    Message Serializers:
"""


class BaseMessageSerializer(serializers.ModelSerializer):
    """
        Base Message Serializer.
    """

    class Meta:
        model = Message
        fields = BaseWhoDidItSerializer.Meta.fields + [
            'thread', 'text', 'is_read'
        ]
        read_only_fields = BaseWhoDidItSerializer.Meta.read_only_fields + [
            'is_read'
        ]
