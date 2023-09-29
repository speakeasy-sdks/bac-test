# Jobs
(*jobs*)

### Available Operations

* [list](#list) - Simply lists jobs.

## list

Returns the first (sorted) #`max_jobs` jobs that belong to the `client_id` passed in the body payload (by default).
If `return_all` is set to true, it returns all jobs on the Bacalhau network.

If `id` is set, it returns only the job with that ID.

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.ListRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    exclude_tags=[
        'Bicycle',
    ],
    id='9304c616-291f-41ad-b862-54e133c0149e',
    include_tags=[
        'Metal',
    ],
    max_jobs=10,
    return_all=False,
    sort_by='created_at',
    sort_reverse=False,
)

res = s.jobs.list(req)

if res.list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.ListRequest](../../models/shared/listrequest.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**

