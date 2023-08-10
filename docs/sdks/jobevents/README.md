# job_events

### Available Operations

* [get](#get) - Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.

## get

Events (e.g. Created, Bid, BidAccepted, ..., ResultsAccepted, ResultsPublished) are useful to track the progress of a job.


### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.EventsRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    filters=shared.EventFilterOptions(
        exclude_execution_level=False,
        exclude_job_level=False,
        since=468651,
    ),
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.job_events.get(req)

if res.events_response is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.EventsRequest](../../models/shared/eventsrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.GetJobEventsResponse](../../models/operations/getjobeventsresponse.md)**
