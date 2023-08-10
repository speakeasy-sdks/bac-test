# results

### Available Operations

* [get](#get) - Returns the results of the job-id specified in the body payload.

## get

Example response:

```json
{
  "results": [
    {
      "NodeID": "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
      "Data": {
        "StorageSource": "IPFS",
        "Name": "job-9304c616-291f-41ad-b862-54e133c0149e-shard-0-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
        "CID": "QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe"
      }
    }
  ]
}
```

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.StateRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.results.get(req)

if res.results_response is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.StateRequest](../../models/shared/staterequest.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.GetResultsResponse](../../models/operations/getresultsresponse.md)**

