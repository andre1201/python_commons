# coding=utf-8
from  __future__ import unicode_literals

import json

from django.db import models
from django.utils.translation import ugettext_lazy as _


class JsonField(models.TextField):
    """
     Преобразует данные python в json при сохранении в базу.
     При получении данных json преобразует в формат python
    """
    description = _('Текстовое поле которые преобразует dict в json и обратно')

    def get_internal_type(self):
        return "JsonField"

    def _check_dict(self, values):
        if not isinstance(values, list):
            values = [values]
        for val in values:
            if not isinstance(val, dict):
                raise Exception("Поле должно быть dict")
        return True

    def pre_save(self, model_instance, add):
        v = super(JsonField, self).pre_save(model_instance, add)
        self._check_dict(v)
        try:
            return json.dumps(v)
        except ValueError as e:
            raise e

    def from_db_value(self, value, expression, connection, context):
        try:
            return json.loads(value)
        except ValueError as e:
            raise Exception("Ошибка при конвертации в dict")
