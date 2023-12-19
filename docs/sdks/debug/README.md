# Debug
(*debug*)

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
    pass
```


### Response

**[operations.GetDebugResponse](../../models/operations/getdebugresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
