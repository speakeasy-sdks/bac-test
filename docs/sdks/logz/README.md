# Logz
(*logz*)

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import bac

s = bac.Bac()


res = s.logz.get()

if res.plain_success is not None:
    # handle response
    pass

```


### Response

**[operations.GetLogzResponse](../../models/operations/getlogzresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
