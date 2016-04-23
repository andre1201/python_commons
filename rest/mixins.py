# coding=utf-8
from __future__ import unicode_literals

from django.core.exceptions import FieldError

from python_commons.utils.decorators import json_logger
from .exeptions import BadRequestError



class FilterMixin(object):
    """
    Фильтрует queryset на основе параметров переданых в строке запроса
        ?id=1&name=name
    Преобразует в строку фильра:
        id=1, name=name
    Возвращает отфильтрованые объекты которые удовлетворяют условию
    """

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if not params:
            return super(FilterMixin, self).filter_queryset(queryset)
        try:
            return queryset.filter(**params.dict())
        except FieldError as e:
            raise BadRequestError("Не корректные параметры для фильтрации. " \
                                  "Описание ошибки:%s" % e.message)


class LoggerMixinView(object):
    """
    Выводит данные в консоль
    """

    @json_logger
    def post(self, request, *args, **kwargs):
        return super(LoggerMixinView, self).post(request, *args, **kwargs)

    @json_logger
    def put(self, request, *args, **kwargs):
        return super(LoggerMixinView, self).put(request, *args, **kwargs)

    @json_logger
    def get(self, request, *args, **kwargs):
        return super(LoggerMixinView, self).get(request, *args, **kwargs)

    @json_logger
    def delete(self, request, *args, **kwargs):
        return super(LoggerMixinView, self).delete(request, *args, **kwargs)

    @json_logger
    def patch(self, request, *args, **kwargs):
        return super(LoggerMixinView, self).patch(request, *args, **kwargs)