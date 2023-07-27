from ..api_service import ApiCharacter
from random import randint


def test_put_characters(api_characters: ApiCharacter):
    #  Find Hero
    heroes = api_characters.get_characters().json()["result"]
    our_hero = heroes[randint(0, len(heroes))]
    new_identity = "okay"

    #  Update hero information with new identity
    api_characters.put_character(
        our_hero["name"],
        our_hero["universe"],
        our_hero["education"],
        our_hero["weight"],
        our_hero["height"],
        new_identity
    )

    #  Check that hero is updated
    get_hero = api_characters.get_character(our_hero["name"]).json()["result"]
    assert get_hero["identity"] == new_identity
