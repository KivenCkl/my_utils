'''
Author       : ChenKailun
Date         : 2021-02-09 19:38
LastEditTime : 2021-02-09 20:50
FilePath     : /python/cache.py
Description  :
'''
from itertools import permutations

try:
    from functools import cached_property
except ImportError:

    class cached_property:  # noqa
        def __init__(self, func):
            self.__doc__ = getattr(func, "__doc__")
            self.func = func

        def __get__(self, obj, cls):
            if obj is None:
                return self
            value = obj.__dict__[self.func.__name__] = self.func(obj)
            return value


class Test:
    def __init__(self, value=None):
        self._value = value

    @cached_property
    def test(self):
        return list(permutations([i for i in range(self._value)], self._value))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
