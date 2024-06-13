from rest_framework import serializers
from apps_generic.whodidit.models import WhoDidIt


class BaseWhoDidItSerializer(serializers.ModelSerializer):
    """
       Serializer for the WhoDidIt model, providing basic serialization of the auditing fields.
    """
    class Meta:
        model = WhoDidIt
        fields = [
            'id',

            'created_on', 'created_by',

            'updated_on', 'updated_by',
        ]
        read_only_fields = [
            'created_on', 'created_by',

            'updated_on', 'updated_by',
        ]
