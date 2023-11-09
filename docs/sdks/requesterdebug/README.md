# RequesterDebug
(*requester_debug*)

### Available Operations

* [get](#get) - Returns debug information on what the current node is doing.

## get

Returns debug information on what the current node is doing.

### Example Usage

```python
import bac

s = bac.Bac()


res = s.requester_debug.get()

if res.success is not None:
    # handle response
    pass
```


### Response

**[operations.GetRequesterDebugResponse](../../models/operations/getrequesterdebugresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
