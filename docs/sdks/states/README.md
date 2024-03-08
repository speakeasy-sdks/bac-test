# States
(*states*)

### Available Operations

* [get](#get) - Returns the state of the job-id specified in the body payload.

## get

Example response:

```json
{
  "state": {
    "Nodes": {
      "QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86": {
        "Shards": {
          "0": {
            "NodeId": "QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86",
            "State": "Cancelled",
            "VerificationResult": {},
            "PublishedResults": {}
          }
        }
      },
      "QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3": {
        "Shards": {
          "0": {
            "NodeId": "QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3",
            "State": "Cancelled",
            "VerificationResult": {},
            "PublishedResults": {}
          }
        }
      },
      "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL": {
        "Shards": {
          "0": {
            "NodeId": "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
            "State": "Completed",
            "Status": "Got results proposal of length: 0",
            "VerificationResult": {
              "Complete": true,
              "Result": true
            },
            "PublishedResults": {
              "StorageSource": "IPFS",
              "Name": "job-9304c616-291f-41ad-b862-54e133c0149e-shard-0-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
              "CID": "QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe"
            },
            "RunOutput": {
              "stdout": "Thu Nov 17 13:32:55 UTC 2022\n",
              "stdouttruncated": false,
              "stderr": "",
              "stderrtruncated": false,
              "exitCode": 0,
              "runnerError": ""
            }
          }
        }
      }
    }
  }
}
```

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.StateRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.states.get(req)

if res.state_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.StateRequest](../../models/shared/staterequest.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.GetStatesResponse](../../models/operations/getstatesresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
