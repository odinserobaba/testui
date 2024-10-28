import pytest
import logging
import functools
from APITest import APITest
from decorator import handle_exceptions, log_execution, setup_logger


class TestFirstToken:
    @pytest.fixture(scope='class')
    def user_api_get_token(self):
        base_url = 'lk-test.egais.ru'
        path = "/api-lc-license/tools/token?role=developer"
        headers = {"Accept": "*/*"}
        user_api = APITest(base_url=base_url, path=path, headers=headers)
        user_api.logger.info(
            f"Created {__name__} instance for {base_url}{path}")
        status, response = user_api.get()

        return response

    @handle_exceptions
    @pytest.mark.parametrize("parameter", ["value1", "value2"])
    def test_get_info1(self, user_api_get_token,parameter):

        base_url = 'lk-test.egais.ru'
        headers = {
            "Accept": "*/*",
            "Authorization": f"{user_api_get_token[1:]}"
        }
        get_info = APITest(
            base_url=base_url, path='/api-lc-license/dashboard/license/request/225358/info', headers=headers)
        get_info.add_log(f'Start {__name__}')
        status_info, response_info = get_info.get()
        get_info.add_log(
            f'{__name__} status -> {status_info} response -> {response_info} ')
        get_info.add_log(
            f'{__name__} param -> {parameter}')
        assert status_info == 200

    @handle_exceptions
    @pytest.mark.parametrize("parameter", ["value1", "value2"])
    def test_get_info2(self, user_api_get_token,parameter):

        base_url = 'lk-test.egais.ru'
        headers = {
            "Accept": "*/*",
            "Authorization": f"{user_api_get_token[1:]}"
        }
        get_info = APITest(
            base_url=base_url, path='/api-lc-license/dashboard/license/request/225358/info', headers=headers)
        get_info.add_log(f'Start {__name__}')
        status_info, response_info = get_info.get()
        get_info.add_log(
            f'{__name__} status -> {status_info} response -> {response_info} ')
        get_info.add_log(
            f'{__name__} param -> {parameter}')
        assert status_info == 200
