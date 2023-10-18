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


## cancel

Cancels a job specified by `id` as long as that job belongs to `client_id`.

Returns the current jobstate after the cancel request has been processed.

### Example Usage

```python
import bac
from bac.models import shared

s = bac.Bac()

req = shared.CancelRequest(
    client_public_key='Clifton',
    payload=shared.JobCancelPayload(
        client_id='powder',
        job_id='AI',
    ),
    signature='East',
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
    client_public_key='sad',
    payload=shared.JobCreatePayload(
        api_version='V1beta1',
        client_id='challenge',
        spec=shared.Spec(
            annotations=[
                'Oriental',
            ],
            deal=shared.Deal(),
            docker=shared.JobSpecDocker(
                entrypoint=[
                    'Gasoline',
                ],
                environment_variables=[
                    'seriously',
                ],
                parameters=[
                    'Representative',
                ],
            ),
            inputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "less": 'Steel',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
            ],
            network=shared.NetworkConfig(
                domains=[
                    'TLS',
                ],
            ),
            node_selectors=[
                shared.LabelSelectorRequirement(
                    values=[
                        'West',
                    ],
                ),
            ],
            outputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "Licensed": 'Shoes',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
            ],
            publisher_spec=shared.PublisherSpec(
                params={
                    "website": 'calculating',
                },
            ),
            resources=shared.ResourceUsageConfig(),
            wasm=shared.JobSpecWasm(
                entry_module=shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "Southeast": 'synthesizing',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    s3=shared.S3StorageSpec(),
                ),
                environment_variables={
                    "blue": 'North',
                },
                import_modules=[
                    shared.StorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "lavender": 'Berkshire',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        s3=shared.S3StorageSpec(),
                    ),
                ],
                parameters=[
                    'quantify',
                ],
            ),
        ),
    ),
    signature='Chair',
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

