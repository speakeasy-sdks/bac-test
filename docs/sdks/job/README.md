# Job
(*job*)

### Available Operations

* [approve](#approve) - Approves a job to be run on this compute node.
* [cancel](#cancel) - Cancels the job with the job-id specified in the body payload.
* [submit](#submit) - Submits a new job to the network.

## approve

Approves a job to be run on this compute node.

### Example Usage

```python
import bac

s = bac.Bac()


res = s.job.approve()

if res.success is not None:
    # handle response
    pass
```


### Response

**[operations.ApproveJobResponse](../../models/operations/approvejobresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## cancel

Cancels a job specified by `id` as long as that job belongs to `client_id`.

Returns the current jobstate after the cancel request has been processed.

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.CancelRequest(
    client_public_key='string',
    payload=shared.JobCancelPayload(
        client_id='string',
        job_id='string',
    ),
    signature='string',
)

res = s.job.cancel(req)

if res.cancel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.CancelRequest](../../models/shared/cancelrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CancelJobResponse](../../models/operations/canceljobresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## submit

Description:

* `client_public_key`: The base64-encoded public key of the client.
* `signature`: A base64-encoded signature of the `data` attribute, signed by the client.
* `payload`:
    * `ClientID`: Request must specify a `ClientID`. To retrieve your `ClientID`, you can do the following: (1) submit a dummy job to Bacalhau (or use one you created before), (2) run `bacalhau describe <job-id>` and fetch the `ClientID` field.
	* `APIVersion`: e.g. `"V1beta1"`.
    * `Spec`: https://github.com/bacalhau-project/bacalhau/blob/main/pkg/model/job.go


### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.SubmitRequest(
    client_public_key='string',
    payload=shared.JobCreatePayload(
        api_version='V1beta1',
        client_id='string',
        spec=shared.Spec(
            annotations=[
                'string',
            ],
            deal=shared.Deal(),
            docker=shared.JobSpecDocker(
                entrypoint=[
                    'string',
                ],
                environment_variables=[
                    'string',
                ],
                parameters=[
                    'string',
                ],
            ),
            inputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        'key': 'string',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
            ],
            network=shared.NetworkConfig(
                domains=[
                    'string',
                ],
            ),
            node_selectors=[
                shared.LabelSelectorRequirement(
                    values=[
                        'string',
                    ],
                ),
            ],
            outputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        'key': 'string',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
            ],
            publisher_spec=shared.PublisherSpec(
                params={
                    'key': 'string',
                },
            ),
            resources=shared.ResourceUsageConfig(),
            wasm=shared.JobSpecWasm(
                entry_module=shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        'key': 'string',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
                environment_variables={
                    'key': 'string',
                },
                import_modules=[
                    shared.StorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            'key': 'string',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        s3=shared.S3StorageSpec(),
                    ),
                ],
                parameters=[
                    'string',
                ],
            ),
        ),
    ),
    signature='string',
)

res = s.job.submit(req)

if res.submit_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.SubmitRequest](../../models/shared/submitrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.SubmitJobResponse](../../models/operations/submitjobresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
