# addok_multiple_result_name

[Addok](https://github.com/etalab/addok) plugin to monkey patch the class `addok.core.Result` to let `__getattr__` to return "name" property as list.

## Addressed problem

The default core code only pick the first `name` from the document, let's keep all.

Then keep only the first one as a plugin.

## Configuration

Add `addok_multiple_result_name.first_name`.

```
SEARCH_RESULT_PROCESSORS_PYPATHS = [
    ...
    'addok_multiple_result_name.first_name',  # Also apply the monkey patch at import time
    ...
```
