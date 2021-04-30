# Not again!

Memoize any function with this lightweight decorator, even across runs. It stores results in memory and disk.

Get it.

    pip install notagain

Use it.

```python
from notagain import memoize

@memoize()
def expensive_function(arg, kwarg=None):
  # i.e. some boring query
  return arg
```

Control it.

```python
@memoize(cache_dir='tmp', memory_cache=True, disk_cache=True)
```

You can change the pickles path. You can deactivate memory and/or disk cache.

## About the name

https://www.youtube.com/watch?v=SOBNO4gl_yM
