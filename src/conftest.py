import pytest

from settings import Settings
from .api_service import ApiCharacter


@pytest.fixture(name="api_host", scope="session")
def get_host() -> str:
    return Settings.API_HOST


@pytest.fixture(name="auth_data", scope="session")
def get_auth_data() -> tuple:
    return (Settings.LOGIN, Settings.PASSWORD)


@pytest.fixture(name="api_characters", scope="session")
def api_characters(api_host, auth_data):
    return ApiCharacter(api_host, auth_data)


@pytest.fixture()
def delete_all_heroes(api_characters: ApiCharacter):
    heroes = api_characters.get_characters().json()["result"]
    if heroes:
        for hero in heroes:
            api_characters.delete_character(hero["name"])


@pytest.fixture(autouse=True, scope="session")
def reset_system_state(api_characters: ApiCharacter):
    api_characters.reset_state()
    yield
    api_characters.reset_state()
