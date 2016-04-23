# coding=utf-8
import os
from abc import ABCMeta, abstractmethod

DGANGO_DEBUG_MODE = "DJANGO_DEBUG_MODE"


class Cheker(object):
    __metaclass__ = ABCMeta

    value = ["True", "true", "TRUE"]

    @abstractmethod
    def check(self):
        """
        Метод должен возвращать булевое значение.
        Проверяет DJANGO_DEBUG_MODE
        """

    @property
    def environ(self):
        return os.environ.get(DGANGO_DEBUG_MODE)


class IsProduction(Cheker):
    def check(self):
        if self.environ not in self.value:
            return True


class IsDevelop(Cheker):
    def check(self):
        if self.environ in self.value:
            return True
