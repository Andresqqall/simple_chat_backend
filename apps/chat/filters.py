from django_filters.rest_framework import FilterSet, filters

from apps.chat.models import Thread


class ChatFilter(FilterSet):
    class Meta:
        model = Thread
        fields = ['participants']

    base_filters = filters.CharFilter(method="with_base_filters")

    @staticmethod
    def with_base_filters(qs, name, value):
        return qs.with_default_filters()
