<!-- Start SDK Example Usage -->


```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.VersionRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
)

res = s.build_version.get(req)

if res.version_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->