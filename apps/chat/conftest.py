from typing import Dict

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def chat_payload(second_user: User) -> Dict:
    """
    Fixture to generate a valid chat payload with one participant.
    """
    return dict(
        participants=[second_user.id]
    )


@pytest.fixture
def chat_payload_with_overload_participants(second_user: User) -> Dict:
    """
    Fixture to generate an invalid chat payload with too many participants.
    """
    # Assuming an overload means having more than the allowed number of participants
    # Here, we simulate having double the user ID, but normally you would add multiple users
    return dict(
        participants=[second_user.id, second_user.id, second_user.id]
    )
