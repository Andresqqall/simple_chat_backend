from django.db.models import Q, Count
from rest_framework import status
from drf_rw_serializers import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.chat.filters import ChatFilter
from apps.chat.models import Thread, Message
from apps.chat.serializers import (
    DetailThreadSerializer,
    BaseThreadSerializer,
    CreateTreadSerializer,

    BaseMessageSerializer,
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
        """
        Returns all threads.
        """
        return Thread.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Creates a new thread or retrieves an existing one.
        """
        write_serializer = self.get_write_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)

        validated_data = write_serializer.validated_data
        participants = [validated_data['participants'][0].id, request.user.id]
        thread = Thread.objects.filter(
            participants__id__in=participants
        ).annotate(num_chats=Count('participants')).filter(
            num_chats=len(participants)
        ).first()

        if thread:
            write_serializer = self.read_serializer_class(thread)
        else:
            self.perform_create(write_serializer)

        read_serializer = self.get_read_serializer(write_serializer.instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        Adds the request user to the thread participants and saves the new thread.
        """
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
        """
        Retrieves a thread by its primary key.
        """
        return get_object_or_404(Thread, pk=self.kwargs['thread_pk'])


class ThreadHistoryMessageListAPIView(generics.ListAPIView):
    """
    API view to list messages in a thread with read status update.
    """
    serializer_class = BaseMessageSerializer

    def get_queryset(self):
        """
        Returns messages for a specific thread.
        """
        thread_pk = self.kwargs['thread_pk']
        return Message.objects.filter(thread__pk=thread_pk)

    def paginate_queryset(self, queryset):
        """
        Updates the read status of messages and paginates the queryset.
        """
        paginated_qs = super().paginate_queryset(queryset)

        if paginated_qs is not None:
            user = self.request.user
            message_ids = [message.id for message in paginated_qs]
            queryset.filter(Q(id__in=message_ids) & Q(is_read=False) & ~Q(created_by=user)).update(is_read=True)

        return super().paginate_queryset(queryset)


class MessageCreateAPIView(generics.CreateAPIView):

    serializer_class = BaseMessageSerializer
