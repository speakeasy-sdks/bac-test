# Readyz

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import bac


s = bac.Bac()


res = s.readyz.get()

if res.plain_success is not None:
    # handle response
```


### Response

**[operations.GetReadyzResponse](../../models/operations/getreadyzresponse.md)**

