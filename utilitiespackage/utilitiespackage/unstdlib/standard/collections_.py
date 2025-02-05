from collections import MutableMapping, OrderedDict
from threading import Lock

_Null = object()


# This object is maintained under the urllib3 codebase.
class RecentlyUsedContainer(MutableMapping):
    """
    Provides a thread-safe dict-like container which maintains up to
    ``maxsize`` keys while throwing away the least-recently-used keys beyond
    ``maxsize``.

    :param maxsize:
        Maximum number of recent elements to retain.

    :param dispose_func:
        Every time an item is evicted from the container,
        ``dispose_func(value)`` is called.  Callback which will get called
    """

    ContainerCls = OrderedDict

    def __init__(self, maxsize=10, dispose_func=None):
        self._maxsize = maxsize
        self.dispose_func = dispose_func

        self._container = self.ContainerCls()
        self._lock = Lock()

    def __getitem__(self, key):
        # Re-insert the item, moving it to the end of the eviction line.
        with self._lock:
            item = self._container.pop(key)
            self._container[key] = item
            return item

    def __setitem__(self, key, value):
        evicted_value = _Null
        with self._lock:
            # Possibly evict the existing value of 'key'
            evicted_value = self._container.get(key, _Null)
            self._container[key] = value

            # If we didn't evict an existing value, we might have to evict the
            # least recently used item from the beginning of the container.
            if len(self._container) > self._maxsize:
                _key, evicted_value = self._container.popitem(last=False)

        if self.dispose_func and evicted_value is not _Null:  # pragma: no cover
            self.dispose_func(evicted_value)

    def __delitem__(self, key):
        with self._lock:  # pragma: no cover
            value = self._container.pop(key)

        if self.dispose_func:  # pragma: no cover
            self.dispose_func(value)

    def __len__(self):
        with self._lock:  # pragma: no cover
            return len(self._container)

    def __iter__(self):
        raise NotImplementedError("Iteration over this class is unlikely to be threadsafe.")  # pragma: no cover

    def clear(self):
        with self._lock:  # pragma: no cover
            # Copy pointers to all values, then wipe the mapping
            # under Python 2, this copies the list of values twice :-|
            values = list(self._container.values())
            self._container.clear()

        if self.dispose_func:  # pragma: no cover
            for value in values:
                self.dispose_func(value)

    def keys(self):
        with self._lock:  # pragma: no cover
            return self._container.keys()
