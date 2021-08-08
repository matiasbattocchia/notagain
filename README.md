# Not again!

Memoize any function with this lightweight decorator, even across runs. It stores results in memory and disk.

The decorator makes use of the Pickle module to store (and retrieve) function results in a local cache folder.

Memoization is sensible to the function **input arguments** and **source code**, if any of these change
the function gets executed and its output cached.

### Get it

    pip install notagain

### Use it

```python
from notagain import memoize

@memoize()
def expensive_function(arg, kwarg=None):
  # i.e. some boring query
  return arg
```

### Control it

You can change the pickles path. You can deactivate memory and/or disk cache.

```python
@memoize(cache_dir='tmp', memory_cache=True, disk_cache=True)
```

If you would like to disable this library info messages.

```python
logging.getLogger('notagain').setLevel('WARNING')
```

## About the name

https://www.youtube.com/watch?v=SOBNO4gl_yM
