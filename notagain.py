'''Memory and disk cache for functions'''

__version__ = '0.3'

import functools
from hashlib import md5
from pathlib import Path
import os
import inspect
import pickle
import logging
import copy

logger = logging.getLogger(__name__)

def memoize(
        cache_dir='tmp',
        memory_cache=True,
        disk_cache=True,
        invalidate_cache=False,
    ):
    '''
    cache_dir : str
        Cache path where to store Pickle files.

    memory_cache : bool
        Whether if memory cache is active.

    disk_cache : bool
        Whether if disk cache is active.

    invalidate_cache : bool
        If true, calculates and caches function in memory and/or disk, no matter if a
        cached version exists.

    Note: If both memory and disk caches are inactive, then memoize behaves as the
    wrapped function.
    '''
    def decorator(func):
        cache = dict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            hasher = md5()

            hasher.update( inspect.getsource(func).encode() )
            [hasher.update( pickle.dumps(a) ) for a in args]
            {hasher.update( pickle.dumps(v) ) for k,v in kwargs.items()}

            key = hasher.hexdigest()

            path = Path(cache_dir) / func.__name__
            path.mkdir(parents=True, exist_ok=True)
            path /= f'{key}.pkl'

            # memory cache
            if not invalidate_cache and key in cache:
                result = copy.deepcopy(cache[key])
                logger.info(f'Memory cache hit for {func.__name__} with key {key}.')

            # disk cache
            elif not invalidate_cache and path.is_file():
                result = pickle.load( open(path, 'rb') )
                logger.info(f'Disk cache hit for {func.__name__} with path {path}.')

                if memory_cache:
                    cache[key] = copy.deepcopy(result)

            # evaluate function
            else:
                result = func(*args, **kwargs)
                logger.info(f'Cache miss for {func.__name__} with key {key}.')

                if memory_cache:
                    cache[key] = copy.deepcopy(result)

                if disk_cache:
                    pickle.dump( result, open(path, 'wb') )

            return result

        if not memory_cache and not disk_cache:
            return func

        return wrapper

    return decorator
