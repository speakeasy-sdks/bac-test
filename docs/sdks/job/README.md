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
    client_public_key='corrupti',
    payload=shared.JobCancelPayload(
        client_id='provident',
        job_id='distinctio',
        reason='quibusdam',
    ),
    signature='unde',
)

res = s.job.cancel(req)

if res.cancel_response is not None:
    # handle response
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
    client_public_key='nulla',
    payload=shared.JobCreatePayload(
        api_version='V1beta1',
        client_id='corrupti',
        spec=shared.Spec(
            annotations=[
                'illum',
            ],
            deal=shared.Deal(
                concurrency=423655,
                targeting_mode=False,
            ),
            do_not_track=False,
            docker=shared.JobSpecDocker(
                entrypoint=[
                    'error',
                ],
                environment_variables=[
                    'deserunt',
                ],
                image='suscipit',
                parameters=[
                    'iure',
                ],
                working_directory='magnam',
            ),
            engine=shared.Engine.ENGINE_DONE,
            inputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "ipsa": 'delectus',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='tempora',
                    read_write=False,
                    repo='suscipit',
                    s3=shared.S3StorageSpec(
                        bucket='molestiae',
                        checksum='minus',
                        endpoint='placeat',
                        key='voluptatum',
                        region='iusto',
                        version_id='excepturi',
                    ),
                    source_path='nisi',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_DONE,
                    url='temporibus',
                ),
            ],
            network=shared.NetworkConfig(
                domains=[
                    'ab',
                ],
                type=shared.Network.NETWORK_FULL,
            ),
            node_selectors=[
                shared.LabelSelectorRequirement(
                    key='veritatis',
                    operator=shared.SelectionOperator.NOT_IN,
                    values=[
                        'perferendis',
                    ],
                ),
            ],
            outputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "ipsam": 'repellendus',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='sapiente',
                    read_write=False,
                    repo='quo',
                    s3=shared.S3StorageSpec(
                        bucket='odit',
                        checksum='at',
                        endpoint='at',
                        key='maiores',
                        region='molestiae',
                        version_id='quod',
                    ),
                    source_path='quod',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_URL_DOWNLOAD,
                    url='totam',
                ),
            ],
            publisher=shared.Publisher.PUBLISHER_S3,
            publisher_spec=shared.PublisherSpec(
                params={
                    "dolorum": 'dicta',
                },
                type=shared.Publisher.PUBLISHER_S3,
            ),
            resources=shared.ResourceUsageConfig(
                cpu='officia',
                disk='occaecati',
                gpu='fugit',
                memory='deleniti',
            ),
            timeout=944669,
            wasm=shared.JobSpecWasm(
                entry_module=shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "optio": 'totam',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='beatae',
                    read_write=False,
                    repo='commodi',
                    s3=shared.S3StorageSpec(
                        bucket='molestiae',
                        checksum='modi',
                        endpoint='qui',
                        key='impedit',
                        region='cum',
                        version_id='esse',
                    ),
                    source_path='ipsum',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_ESTUARY,
                    url='aspernatur',
                ),
                entry_point='perferendis',
                environment_variables={
                    "ad": 'natus',
                },
                import_modules=[
                    shared.StorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "sed": 'iste',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='dolor',
                        read_write=False,
                        repo='natus',
                        s3=shared.S3StorageSpec(
                            bucket='laboriosam',
                            checksum='hic',
                            endpoint='saepe',
                            key='fuga',
                            region='in',
                            version_id='corporis',
                        ),
                        source_path='iste',
                        storage_source=shared.StorageSourceType.STORAGE_SOURCE_URL_DOWNLOAD,
                        url='saepe',
                    ),
                ],
                parameters=[
                    'quidem',
                ],
            ),
        ),
    ),
    signature='architecto',
)

res = s.job.submit(req)

if res.submit_response is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.SubmitRequest](../../models/shared/submitrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.SubmitJobResponse](../../models/operations/submitjobresponse.md)**

