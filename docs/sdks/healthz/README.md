# Healthz

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import bac


s = bac.Bac()


res = s.healthz.get()

if res.health_info is not None:
    # handle response
```


### Response

**[operations.GetHealthzResponse](../../models/operations/gethealthzresponse.md)**

