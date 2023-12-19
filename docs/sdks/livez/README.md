# Livez
(*livez*)

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import bac

s = bac.Bac()


res = s.livez.get()

if res.plain_success is not None:
    # handle response
    pass
```


### Response

**[operations.GetLivezResponse](../../models/operations/getlivezresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
