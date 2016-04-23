# coding=utf-8
from __future__ import unicode_literals

from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):
    """
        Добавлет пользовтаеля из сессии в данные
        для последующего сохранения

            :var user_filed_name - имя поля объекта User
    """
    user_filed_name = 'owner'

    def to_internal_value(self, data):
        user = self.context['request'].user.id
        if not isinstance(data, list):
            data[self.user_filed_name] = user
            return super(OwnerSerializer, self).to_internal_value(data)
        result = {}
        for k, v in data.iteriems():
            result[k] = v
            result[self.user_filed_name] = user
        return super(OwnerSerializer, self).to_internal_value(result)
