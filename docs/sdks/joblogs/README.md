# JobLogs
(*job_logs*)

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
    client_public_key='<value>',
    payload=shared.LogsPayload(
        client_id='<value>',
        execution_id='<value>',
        job_id='<value>',
    ),
    signature='<value>',
)

res = s.job_logs.display(req)

if res.success is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.LogRequest](../../models/shared/logrequest.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.DisplayJobLogsResponse](../../models/operations/displayjoblogsresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
