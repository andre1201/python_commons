# coding=utf-8
from __future__ import unicode_literals

from rest_framework import exceptions, status


class ApiExeption(exceptions.APIException):
    def __init__(self, detail="Сервер не доступен", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.status_code = status_code
        super(ApiExeption, self).__init__(detail)


class BadRequestError(ApiExeption):
    def __init__(self, detail="Не корректный запрос."):
        super(BadRequestError, self).__init__(detail, status.HTTP_400_BAD_REQUEST)
