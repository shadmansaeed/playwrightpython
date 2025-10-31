import pytest


@pytest.fixture(scope="session")
def user_credentials(request):  # here request is global parameter
    return request.param