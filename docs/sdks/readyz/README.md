# readyz

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.readyz.get()

if res.plain_success is not None:
    # handle response
```


### Response

**[operations.GetReadyzResponse](../../models/operations/getreadyzresponse.md)**

