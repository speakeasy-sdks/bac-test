# healthz

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.healthz.get()

if res.health_info is not None:
    # handle response
```


### Response

**[operations.GetHealthzResponse](../../models/operations/gethealthzresponse.md)**
