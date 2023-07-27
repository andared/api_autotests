from ..api_service import ApiCharacter


def test_delete_character(api_characters: ApiCharacter):
    #  Create new character
    name = "Test Brother"
    api_characters.post_character(name, "a b", "c d", 0.1, 0.2)

    #  Delete created character
    api_characters.delete_character(name)

    #  Check that it deleted
    characters = api_characters.get_characters().json()["result"]
    for character in characters:
        assert character["name"] != name
