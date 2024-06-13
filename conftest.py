from dataclasses import dataclass

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@dataclass
class BaseUserCreds:
    """
    Base data class for user credentials.
    """
    username: str = 'Default'
    first_name: str = 'Test First Name'
    last_name: str = 'Test Last Name'
    email: str = 'default_user@gmail.com'
    password: str = 'P@5gga@@5gf'


@pytest.fixture
def first_user_creds() -> BaseUserCreds:
    """
    Fixture to provide first user credentials.
    """
    @dataclass
    class LegalUserCreds(BaseUserCreds):
        username: str = 'Test User (1)'
        email: str = 'first@gmai.com'

    return LegalUserCreds()


@pytest.fixture
def second_user_creds() -> BaseUserCreds:
    """
    Fixture to provide second user credentials.
    """
    @dataclass
    class DoctorUserCreds(BaseUserCreds):
        username: str = 'Test User (2)'
        email: str = 'second@gmai.com'

    return DoctorUserCreds()


@pytest.fixture(autouse=True)
def create_user(django_user_model) -> User:
    """
    Fixture to create a user instance.
    """
    def _create_user(credentials: BaseUserCreds, client) -> User:
        return django_user_model.objects.create_user(
            email=credentials.email,
            username=credentials.username,
            password=credentials.password,
        )

    return _create_user


@pytest.fixture
def first_user(create_user, client, first_user_creds) -> User:
    """
    Fixture to provide a first user instance.
    """
    user = create_user(first_user_creds, client)
    client.force_login(user)
    return user


@pytest.fixture
def second_user(create_user, client, second_user_creds) -> User:
    """
    Fixture to provide a second user instance.
    """
    user = create_user(second_user_creds, client)
    client.force_login(user)
    return user
