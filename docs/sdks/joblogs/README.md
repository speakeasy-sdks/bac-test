# job_logs

### Available Operations

* [display](#display) - Displays the logs for a current job/execution

## display

Shows the output from the job specified by `id` as long as that job belongs to `client_id`.

The ouput will be continuous until either, the client disconnects or the execution completes.

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.LogRequest(
    client_public_key='praesentium',
    payload=shared.LogsPayload(
        client_id='voluptatibus',
        execution_id='ipsa',
        follow=False,
        job_id='omnis',
        with_history=False,
    ),
    signature='voluptate',
)

res = s.job_logs.display(req)

if res.success is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.LogRequest](../../models/shared/logrequest.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.DisplayJobLogsResponse](../../models/operations/displayjoblogsresponse.md)**

