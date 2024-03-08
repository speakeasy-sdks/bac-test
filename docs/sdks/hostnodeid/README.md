# HostNodeID
(*host_node_id*)

### Available Operations

* [get](#get) - Returns the id of the host node.

## get

Returns the id of the host node.

### Example Usage

```python
import bac

s = bac.Bac()


res = s.host_node_id.get()

if res.plain_success is not None:
    # handle response
    pass

```


### Response

**[operations.GetHostNodeIDResponse](../../models/operations/gethostnodeidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
