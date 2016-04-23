# coding=utf-8
from __future__ import unicode_literals

import json
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def json_logger(func):
    """
    Оборачивает HttpResponse
    Ведет информацию о данных
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, HttpResponse):
            return result
        try:
            logger.info(json.dumps(result.data, indent=4))
        except ValueError as e:
            logger.info(e.message)
        return result

    return wrapper
