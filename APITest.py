import http.client
import urllib.parse
import logging
import inspect
from decorator import handle_exceptions, log_execution
import ssl


class APITest:
    _logger = None

    def __init__(self, base_url, path, headers=None, params=None, body=""):
        self._base_url = base_url
        self._path = path
        self._params = params or {}
        self._headers = headers or {}
        self._body = body
        self._response = None
        self.logger = self._get_logger()

    @classmethod
    def _get_logger(cls):
        if cls._logger is None:
            cls._logger = cls._setup_logger()
        return cls._logger

    @classmethod
    def _setup_logger(cls):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('api_test.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger


    def get(self, headers={}):
        method_name = inspect.currentframe().f_code.co_name
        conn = http.client.HTTPSConnection(
            self._base_url, context=ssl._create_unverified_context())
        query_params = urllib.parse.urlencode(self._params)
        self.logger.info(f"{method_name} -_base_url {self._base_url} _path {
                         self._path} _headers {self._headers} query_params {query_params} ")
        if self._headers:
            conn.request("GET", f"{self._path}", headers=self._headers)
        else:
            conn.request("GET", f"{self._path}", headers=headers)
        response = conn.getresponse()
        res = response.read()
        status = response.status

        self.logger.info(
            f"Result {method_name} -status {response.status} response.read {response.read()}")
        return status, res

    def post(self, body=""):
        conn = http.client.HTTPSConnection(
            self._base_url, context=ssl._create_unverified_context())
        headers = self._headers
        method_name = inspect.currentframe().f_code.co_name
        self.logger.info(f"Start {
                         method_name} -_base_url {self._base_url} _path {self._path} _headers {self._headers}")
        try:
            conn.request("POST", self._path, body=body, headers=headers)
            self.logger.info(f'{method_name} conn {
                             conn.host} {conn.port} {conn}')
            response = conn.getresponse()
            self._response = response
            self.logger.info(
                f"Result {method_name} -status {response.status} response.read {response.read()}")
            return response.status, response.read()
        except Exception as e:
            self.logger.info(f"Exception occurred in {method_name}: {str(e)}")
            raise

    def patch(self, body=""):
        conn = http.client.HTTPSConnection(
            self._base_url, context=ssl._create_unverified_context())
        headers = self._headers
        method_name = inspect.currentframe().f_code.co_name
        self.logger.info(f"Start {
                         method_name} -_base_url {self._base_url} _path {self._path} _headers {self._headers}")
        try:
            conn.request("PATCH", self._path, body=body, headers=headers)
            self.logger.info(f'{method_name} conn {
                             conn.host} {conn.port} {conn}')
            response = conn.getresponse()
            self._response = response
            self.logger.info(
                f"Result {method_name} -status {response.status} response.read {response.read()}")
            return response.status, response.read()
        except Exception as e:
            self.logger.info(f"Exception occurred in {method_name}: {str(e)}")
            raise
    
    def add_log(self,message):
        self.logger.info(message)

