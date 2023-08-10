# debug

### Available Operations

* [get](#get) - Returns debug information on what the current node is doing.

## get

Returns debug information on what the current node is doing.

### Example Usage

```python
import bac


s = bac.Bac()


res = s.debug.get()

if res.success is not None:
    # handle response
```


### Response

**[operations.GetDebugResponse](../../models/operations/getdebugresponse.md)**

