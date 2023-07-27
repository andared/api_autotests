import logging

from pytest_schema import schema, SchemaError


class Utils:

    @staticmethod
    def schema_assert(resp: dict, schemas: dict) -> bool:
        try:
            schema(schemas).exact(resp)
            return True
        except SchemaError as e:
            logging.warning(f"\n{e}")
            return False
