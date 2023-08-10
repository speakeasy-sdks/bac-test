# host_node_id

### Available Operations

* [get](#get) - Returns the id of the host node.

## get

Returns the id of the host node.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.host_node_id.get()

if res.plain_success is not None:
    # handle response
```


### Response

**[operations.GetHostNodeIDResponse](../../models/operations/gethostnodeidresponse.md)**

