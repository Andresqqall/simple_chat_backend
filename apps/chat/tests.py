from rest_framework import status
from rest_framework.reverse import reverse


class TestThreadListCreateAPIView:
    """
    Test suite for ThreadListCreateAPIView.
    """

    url = reverse('chats')

    def test_retrieve_chats_list(self, client, first_user):
        """
        Test retrieving the list of chats.
        """
        response = client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_chat(self, client, first_user, chat_payload):
        """
        Test creating a new chat.
        """
        response = client.post(self.url, data=chat_payload)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_chat_with_overload_participants(self, client, first_user, chat_payload_with_overload_participants):
        """
        Test creating a chat with too many participants.
        """
        response = client.post(self.url, data=chat_payload_with_overload_participants)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


"""
    I'm not covering the whole app with the test above, just a simple example.
"""