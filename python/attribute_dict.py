'''
Author       : ChenKailun
Date         : 2021-03-23 11:44
LastEditTime : 2021-03-23 11:45
FilePath     : /python/attribute_dict.py
Description  :
'''


class AttributeDict(dict):
    """Dictionary subclass enabling attribute lookup/assignment of keys/values.
    For example::
        >>> m = AttributeDict({'foo': 'bar'})
        >>> m.foo
        'bar'
        >>> m.foo = 'not bar'
        >>> m['foo']
        'not bar'
    """
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            pass
        # to conform with __getattr__ spec
        # but get out of the except block so it doesn't look like a nested err
        raise AttributeError(key)

    def set_read_only(self, names, msg="Attribute is read-only"):
        object.__setattr__(self, "_read_only", names)
        object.__setattr__(self, "_read_only_msg", msg)

    def finalize(self, msg="Object is final: No new keys may be added."):
        """Prevent any new keys being set."""
        object.__setattr__(self, "_final", msg)

    def __setitem__(self, key, val):
        if key in self.__dict__.get("_read_only", []):
            raise AttributeError(self._read_only_msg, key)

        final_msg = self.__dict__.get("_final")
        if final_msg and key not in self:
            raise AttributeError(final_msg, key)

        return super(AttributeDict, self).__setitem__(key, val)

    # pylint: disable=inconsistent-return-statements
    def first(self, *names):
        for name in names:
            value = self.get(name)
            if value:
                return value
