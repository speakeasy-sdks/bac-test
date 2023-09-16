# JobLogs

### Available Operations

* [display](#display) - Displays the logs for a current job/execution

## display

Shows the output from the job specified by `id` as long as that job belongs to `client_id`.

The ouput will be continuous until either, the client disconnects or the execution completes.

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.LogRequest(
    client_public_key='reiciendis',
    payload=shared.LogsPayload(
        client_id='est',
        execution_id='mollitia',
        follow=False,
        job_id='laborum',
        with_history=False,
    ),
    signature='dolores',
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

