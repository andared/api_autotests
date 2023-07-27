from ..api_service import ApiCharacter
from ..exceptions import BadRequestException


def test_post_character(api_characters: ApiCharacter):
    #  Given data
    name = "Unique nickname"
    universe = "Somewhere"
    education = "Full"
    weight = 96.547457
    height = 178.2353

    #  Create hero
    response = api_characters.post_character(name, universe, education, weight, height)
    result = response.json()["result"]
    assert result
    assert result["name"] == name
    assert result["universe"] == universe
    assert result["education"] == education
    assert result["weight"] == weight
    assert result["height"] == height

    #  Check that hero created
    hero = api_characters.get_character(name).json()["result"]
    assert hero["name"] == name


def test_501_post_character(api_characters: ApiCharacter):
    heroes_count = len(api_characters.get_characters().json()["result"])

    universe = "Somewhere"
    education = "Full"
    weight = 96.547457
    height = 178.2353

    for _ in range(500 - heroes_count):
        api_characters.post_character(
            name=str(_),
            universe=universe,
            education=education,
            weight=weight,
            height=height
        )

    #  Try to create 501-st hero
    try:
        api_characters.post_character(
            name=str(501),
            universe=universe,
            education=education,
            weight=weight,
            height=height
        )
    except BadRequestException:
        return
    else:
        assert False, "501 hero in DB"


def test_break_validate_post_character(api_characters: ApiCharacter):
    #  Given data
    name = ""
    universe = "Somewhere"
    education = "Full"
    weight = 96.547457
    height = 178.2353

    #  Create hero with broken data
    try:
        api_characters.post_character(name, universe, education, weight, height)
        assert False, "Expected 400 status code"
    except BadRequestException:
        return
