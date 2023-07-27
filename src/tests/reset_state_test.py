from ..api_service import ApiCharacter


def test_reset_state(api_characters: ApiCharacter):
    api_characters.reset_state()

    assert api_characters.get_characters().json()["result"]
