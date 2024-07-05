from addok.core import Result
from addok.config import config

# Monkey patch Result.__getattr__ to return "name" as list

def getter(self, key):
    if key == "_id":
        # result._id should load the id whatever the real field used.
        key = config.ID_FIELD
    if key not in self._cache:
        # By convention, in case of multiple values, first value is default
        # value, others are aliases.
        if key == "name":
            value = self._rawattr(key)
        else:
            value = self._rawattr(key)[0]
        self._cache[key] = value
    return self._cache[key]

Result.__getattr__ = getter

# Let's make the module look like a plugin
def noop(helper, result):
    return result
