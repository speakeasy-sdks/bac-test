# nodes

### Available Operations

* [display](#display) - Displays the nodes that this requester knows about

## display

Displays the nodes that this requester knows about

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.nodes.display()

if res.node_infos is not None:
    # handle response
```


### Response

**[operations.DisplayNodesResponse](../../models/operations/displaynodesresponse.md)**

