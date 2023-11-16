# Nodes
(*nodes*)

### Available Operations

* [display](#display) - Displays the nodes that this requester knows about

## display

Displays the nodes that this requester knows about

### Example Usage

```python
import bac

s = bac.Bac()


res = s.nodes.display()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.DisplayNodesResponse](../../models/operations/displaynodesresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
