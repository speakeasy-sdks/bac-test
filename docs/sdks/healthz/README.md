# Healthz
(*healthz*)

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
    pass

```


### Response

**[operations.GetHealthzResponse](../../models/operations/gethealthzresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
