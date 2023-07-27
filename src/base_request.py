import requests
import logging

from requests import ConnectTimeout
from .exceptions import BadRequestException


class BaseRequest:

    method_get = "GET"
    method_post = "POST"
    method_put = "PUT"
    method_delete = "DELETE"

    def __init__(self, host: str, auth: tuple) -> None:
        self.host = host
        self.auth = auth

    def __base_request(
            self,
            method: str,
            url: str,
            timeout=1,
            **kwargs
    ) -> requests.Response:
        try:
            response = requests.request(method=method, url=url, auth=self.auth, **kwargs)
        except ConnectTimeout as e:
            logging.error(f"{e} for {url}")
            raise e
        logging.info(
            f"{response.status_code}  {method}  {url}  " +
            f"{response.elapsed.microseconds / 1000} ms"
        )
        if response.ok:
            pass
        elif str(response.status_code) in ["400", "422"]:
            raise BadRequestException(
                f"{response.status_code}  {method}  {url}  {response.json()}"
            )
        else:
            assert response.ok, f"{response.status_code}  {method}  {url}"
        assert (
            response.elapsed.microseconds / 1000 < (timeout * 1000)
        ), f"{response.elapsed.microseconds / 1000} ms for {url}"
        return response

    def _get(self, url: str, **kwargs):
        return self.__base_request(self.method_get, url, **kwargs)

    def _post(self, url: str, **kwargs):
        return self.__base_request(self.method_post, url, **kwargs)

    def _put(self, url: str, **kwargs):
        return self.__base_request(self.method_put, url, **kwargs)

    def _delete(self, url: str, **kwargs):
        return self.__base_request(self.method_delete, url, **kwargs)
