# Varz
(*varz*)

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import bac

s = bac.Bac()


res = s.varz.get()

if res.varz_success is not None:
    # handle response
    pass

```


### Response

**[operations.GetVarzResponse](../../models/operations/getvarzresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
