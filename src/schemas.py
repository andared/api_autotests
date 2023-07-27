from pytest_schema import Or, Optional


class Schemas:
    get_characters = {
        "result": Or(
            [
                {
                    Optional("education"): str,
                    "height": Or(float, int),
                    Optional("identity"): str,
                    "name": str,
                    Optional("other_aliases"): str,
                    Optional("universe"): str,
                    "weight": Or(float, str)
                }
            ],
            []
        )
    }
    get_character = Or(
        {
            "result": {
                Optional("education"): str,
                "height": Or(float, int),
                Optional("identity"): str,
                "name": str,
                Optional("other_aliases"): str,
                Optional("universe"): str,
                "weight": Or(float, str)
            }
        },
        {
            "error": "No such name"
        }
    )
    post_character = Or(
        {
            "result": {
                "education": str,
                "height": float,
                "identity": str,
                "name": str,
                "universe": str,
                "weight": float
            }
        },
        {
            "error": str
        }
    )
    put_character = Or(
        {
            "result": {
                "education": str,
                "height": float,
                "identity": str,
                "name": str,
                "universe": str,
                "weight": float,
                Optional("other_aliases"): str
            }
        },
        {
            "error": str
        }
    )
    delete_character = Or(
        {
            "result": str
        },
        {
            "error": "No such name"
        }
    )
