from ..api_service import ApiCharacter


def test_get_characters(api_characters: ApiCharacter):
    response = api_characters.get_characters().json()
    assert response["result"]
