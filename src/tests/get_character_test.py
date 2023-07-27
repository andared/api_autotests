from ..api_service import ApiCharacter
from random import randint


def test_get_character(api_characters: ApiCharacter, reset_system_state):
    heroes = api_characters.get_characters().json()["result"]
    our_hero = heroes[randint(0, len(heroes))]

    get_hero = api_characters.get_character(our_hero["name"]).json()["result"]
    for key_out, key_in in zip(our_hero, get_hero):
        assert key_in == key_out
