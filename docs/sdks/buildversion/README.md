# BuildVersion

### Available Operations

* [get](#get) - Returns the build version running on the server.

## get

See https://github.com/bacalhau-project/bacalhau/releases for a complete list of `gitversion` tags.

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.VersionRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
)

res = s.build_version.get(req)

if res.version_response is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.VersionRequest](../../models/shared/versionrequest.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.GetBuildVersionResponse](../../models/operations/getbuildversionresponse.md)**

