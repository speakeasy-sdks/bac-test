# misc

### Available Operations

* [api_server_version](#api_server_version) - Returns the build version running on the server.

## api_server_version

See https://github.com/bacalhau-project/bacalhau/releases for a complete list of `gitversion` tags.

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiVersionRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
)

res = s.misc.api_server_version(req)

if res.publicapi_version_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.PublicapiVersionRequest](../../models/shared/publicapiversionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.APIServerVersionResponse](../../models/operations/apiserverversionresponse.md)**

