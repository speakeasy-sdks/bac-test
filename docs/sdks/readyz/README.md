# Readyz
(*readyz*)

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
    pass
```


### Response

**[operations.GetReadyzResponse](../../models/operations/getreadyzresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
