#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError
import logging

import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class APIException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class Client:
    DOMAIN = 'jisho.org'
    VERSION = 1

    def __init__(self):
        base_url = f'https://{Client.DOMAIN}/api/v{Client.VERSION}'
        self._base_url = base_url

    @staticmethod
    def clean_params(params):
        return {k: v for k, v in params.items() if v is not None}

    def _get(self, url, params=None):
        if params is None:
            params = {}

        params = self.clean_params(params)

        logger.debug(url)

        response = requests.get(
            url,
            params=params,
        )

        try:
            json = response.json()
            if response.status_code != 200:
                raise APIException(response.status_code,
                                   response.content.decode())

            return json
        except JSONDecodeError:
            return response.content.decode()

    def search(self, keyword):
        url = f'{self._base_url}/search/words'
        params = {'keyword': keyword} if keyword else {}
        return self._get(url, params=params)
