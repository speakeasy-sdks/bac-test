# NodeInfo
(*node_info*)

### Available Operations

* [get](#get) - Returns the info of the node.

## get

Returns the info of the node.

### Example Usage

```python
import bac

s = bac.Bac()


res = s.node_info.get()

if res.node_info is not None:
    # handle response
    pass

```


### Response

**[operations.GetNodeInfoResponse](../../models/operations/getnodeinforesponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
