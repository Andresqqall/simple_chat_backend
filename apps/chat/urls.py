from django.urls import path

from apps.chat import views

urlpatterns = [
    # Treads
    path('', views.ThreadListCreateAPIView.as_view(), name='chats'),
    path('<int:thread_pk>/', views.ThreadRetrieveUpdateDestroyAPIView.as_view(), name='update_chat'),

    # Messages
    path('<int:thread_pk>/history/', views.ThreadHistoryMessageListAPIView.as_view(), name='chat_history'),
    path('mark_message/', views.MarkReadMessageAPIView.as_view(), name='mark_message_as_read'),
    path('send_message/', views.MessageCreateAPIView.as_view(), name='send_message')
]
