from .base_request import BaseRequest
from .endpoints import Endpoints
from .utils import Utils
from .schemas import Schemas
from yarl import URL


class ApiCharacter(BaseRequest):

    def get_characters(self):
        url = str(URL(self.host).with_path(Endpoints.CHARACTERS.value))
        response = self._get(url)
        assert Utils.schema_assert(response.json(), Schemas.get_characters)
        return response

    def get_character(self, name: str):
        url = str(URL(self.host).with_path(Endpoints.CHARACTER.value).with_query({"name": name}))
        response = self._get(url)
        assert Utils.schema_assert(response.json(), Schemas.get_character)
        return response

    def post_character(
            self,
            name: str,
            universe: str,
            education: str,
            weight: float | int,
            height: float | int,
            identity="Hoba"
    ):
        url = str(URL(self.host).with_path(Endpoints.CHARACTER.value))
        payload = {
            "name": name,
            "universe": universe,
            "education": education,
            "weight": weight,
            "height": height,
            "identity": identity
        }
        response = self._post(url, json=payload)
        assert Utils.schema_assert(response.json(), Schemas.post_character)
        return response

    def put_character(
            self,
            name: str,
            universe: str,
            education: str,
            weight: int,
            height: float,
            identity="Hoba"
    ):
        url = str(URL(self.host).with_path(Endpoints.CHARACTER.value).with_query({"name": name}))
        payload = {
            "name": name,
            "universe": universe,
            "education": education,
            "weight": weight,
            "height": height,
            "identity": identity
        }
        response = self._put(url, json=payload)
        assert Utils.schema_assert(response.json(), Schemas.put_character)
        return response

    def delete_character(self, name: str):
        url = str(URL(self.host).with_path(Endpoints.CHARACTER.value).with_query({"name": name}))
        response = self._delete(url)
        assert Utils.schema_assert(response.json(), Schemas.delete_character)
        return response

    def reset_state(self):
        url = str(URL(self.host).with_path(Endpoints.RESET.value))
        return self._post(url)
