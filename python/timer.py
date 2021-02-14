'''
Author       : ChenKailun
Date         : 2021-02-09 20:22
LastEditTime : 2021-02-09 20:54
FilePath     : /python/timer.py
Description  :
'''
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def decorator(*arg, **kwargs):
        start_time = time.time()
        ret = func(*arg, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] cost {end_time - start_time}s!")
        return ret

    return decorator


class Timer:
    def __init__(self, func):
        self.__doc__ = getattr(func, "__doc__")
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        ret = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"[{self.func.__name__}] cost {end_time - start_time}s!")
        return ret


@Timer
def test():
    time.sleep(1)


if __name__ == '__main__':
    test()
