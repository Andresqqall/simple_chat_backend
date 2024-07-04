from django.db.models import Count
from rest_framework import status
from drf_rw_serializers import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.chat.filters import ChatFilter
from apps.chat.models import Thread, Message
from apps.chat.serializers import (
    BaseThreadSerializer,
    DetailThreadSerializer,
    CreateTreadSerializer,
    BaseMessageSerializer
)


message_ids = openapi.Parameter(
    name='message_ids',
    in_=openapi.IN_QUERY,
    description="IDs of the messages to be marked as read",
    type=openapi.TYPE_STRING
)


class ThreadListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list and create threads.
    """
    write_serializer_class = CreateTreadSerializer
    serializer_class = write_serializer_class
    read_serializer_class = DetailThreadSerializer
    filterset_class = ChatFilter

    def get_queryset(self):
        return Thread.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Creates a new thread or retrieves an existing one.
        """
        write_serializer = self.get_write_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)

        validated_data = write_serializer.validated_data
        participants = (validated_data['participants'][0].id, request.user.id)
        thread = Thread.objects.filter(participants__id__in=participants).annotate(
            num_chats=Count('participants')
        ).filter(num_chats=len(participants)).first()

        if thread:
            write_serializer = self.read_serializer_class(thread)
        else:
            self.perform_create(write_serializer)

        read_serializer = self.get_read_serializer(write_serializer.instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.validated_data['participants'].append(self.request.user)
        super().perform_create(serializer)


class ThreadRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, and delete a thread.
    """
    write_serializer_class = BaseThreadSerializer
    serializer_class = write_serializer_class
    read_serializer_class = DetailThreadSerializer

    def get_object(self):
        return get_object_or_404(Thread, pk=self.kwargs['thread_pk'])


class ThreadHistoryMessageListAPIView(generics.ListAPIView):
    """
    API view to list messages in a thread with read status update.
    """
    serializer_class = BaseMessageSerializer

    def get_queryset(self):
        thread_pk = self.kwargs['thread_pk']
        return Message.objects.filter(thread__pk=thread_pk)


class MarkReadMessageAPIView(APIView):
    """
    API view to mark a message as read.
    """

    @staticmethod
    @swagger_auto_schema(manual_parameters=[message_ids])
    def post(request, *args, **kwargs):
        message_ids = request.GET.get('message_ids')

        if message_ids is None:
            raise ValidationError(
                detail='The "message_ids" parameter is required and must be set as a query parameter.'
            )

        unread_messages = Message.objects.filter(id__in=message_ids, is_read=False).exclude(created_by=request.user)

        if unread_messages.exists():
            unread_messages.update(is_read=True)

        return Response(status=status.HTTP_200_OK)


class MessageCreateAPIView(generics.CreateAPIView):

    serializer_class = BaseMessageSerializer
