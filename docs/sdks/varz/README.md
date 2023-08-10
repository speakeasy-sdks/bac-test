# varz

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.varz.get()

if res.varz_success is not None:
    # handle response
```


### Response

**[operations.GetVarzResponse](../../models/operations/getvarzresponse.md)**

