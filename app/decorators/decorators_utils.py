from functools import wraps
import logging

logger = logging.getLogger(__name__)


def memory_profile(method):
    import psutil
    import os
    @wraps(method)
    def inner(*args, **kwargs):
        pid = os.getpid()
        py = psutil.Process(pid)
        before = py.memory_info()[0] / (1024.0 ** 2)
        result = method(*args, **kwargs)
        after = py.memory_info()[0] / (1024.0 ** 2)
        logger.info(f"Memory consumed is  {after - before}  for function:  {method.__name__}")
        return result

    return inner


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        logger.info(f'{fn.__name__} ({args_str})   took {elapsed}s to run.')
        return result

    return inner
