# addok_multiple_result_name

[Addok](https://github.com/etalab/addok) plugin to monkey patch the class `addok.core.Result` to let `__getattr__` to return "name" property as list.

## Addressed problem

The default code only pick the first `name` from the document, let's keep all.

## Configuration

Add `addok_multiple_result_name.noop`.

```
SEARCH_RESULT_PROCESSORS_PYPATHS = [
    ...
    'addok_multiple_result_name.noop',  # Do nothing, only apply the monkey patch at import time
    ...
```
