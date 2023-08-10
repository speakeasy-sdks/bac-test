# job

### Available Operations

* [approve](#approve) - Approves a job to be run on this compute node.
* [cancel](#cancel) - Cancels the job with the job-id specified in the body payload.
* [submit](#submit) - Submits a new job to the network.

## approve

Approves a job to be run on this compute node.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


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
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

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
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.SubmitRequest(
    client_public_key='nulla',
    payload=shared.JobCreatePayload(
        api_version='V1beta1',
        client_id='corrupti',
        spec=shared.Spec(
            annotations=[
                'vel',
                'error',
                'deserunt',
                'suscipit',
            ],
            deal=shared.Deal(
                concurrency=437587,
                targeting_mode=False,
            ),
            do_not_track=False,
            docker=shared.JobSpecDocker(
                entrypoint=[
                    'debitis',
                    'ipsa',
                ],
                environment_variables=[
                    'tempora',
                    'suscipit',
                    'molestiae',
                    'minus',
                ],
                image='placeat',
                parameters=[
                    'iusto',
                    'excepturi',
                    'nisi',
                ],
                working_directory='recusandae',
            ),
            engine=shared.Engine.FOUR,
            inputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "veritatis": 'deserunt',
                        "perferendis": 'ipsam',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='repellendus',
                    read_write=False,
                    repo='sapiente',
                    s3=shared.S3StorageSpec(
                        bucket='quo',
                        checksum='odit',
                        endpoint='at',
                        key='at',
                        region='maiores',
                        version_id='molestiae',
                    ),
                    source_path='quod',
                    storage_source=shared.StorageSourceType.EIGHT,
                    url='esse',
                ),
            ],
            network=shared.NetworkConfig(
                domains=[
                    'porro',
                    'dolorum',
                    'dicta',
                ],
                type=shared.Network.TWO,
            ),
            node_selectors=[
                shared.LabelSelectorRequirement(
                    key='occaecati',
                    operator=shared.SelectionOperator.EQUAL_,
                    values=[
                        'hic',
                        'optio',
                        'totam',
                    ],
                ),
                shared.LabelSelectorRequirement(
                    key='beatae',
                    operator=shared.SelectionOperator.IN,
                    values=[
                        'modi',
                        'qui',
                    ],
                ),
                shared.LabelSelectorRequirement(
                    key='impedit',
                    operator=shared.SelectionOperator.EXISTS,
                    values=[
                        'ipsum',
                        'excepturi',
                    ],
                ),
            ],
            outputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "ad": 'natus',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='sed',
                    read_write=False,
                    repo='iste',
                    s3=shared.S3StorageSpec(
                        bucket='dolor',
                        checksum='natus',
                        endpoint='laboriosam',
                        key='hic',
                        region='saepe',
                        version_id='fuga',
                    ),
                    source_path='in',
                    storage_source=shared.StorageSourceType.THREE,
                    url='iste',
                ),
            ],
            publisher=shared.Publisher.TWO,
            publisher_spec=shared.PublisherSpec(
                params={
                    "quidem": 'architecto',
                    "ipsa": 'reiciendis',
                    "est": 'mollitia',
                    "laborum": 'dolores',
                },
                type=shared.Publisher.ONE,
            ),
            resources=shared.ResourceUsageConfig(
                cpu='corporis',
                disk='explicabo',
                gpu='nobis',
                memory='enim',
            ),
            timeout=607831,
            wasm=shared.JobSpecWasm(
                entry_module=shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "minima": 'excepturi',
                        "accusantium": 'iure',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='culpa',
                    read_write=False,
                    repo='doloribus',
                    s3=shared.S3StorageSpec(
                        bucket='sapiente',
                        checksum='architecto',
                        endpoint='mollitia',
                        key='dolorem',
                        region='culpa',
                        version_id='consequuntur',
                    ),
                    source_path='repellat',
                    storage_source=shared.StorageSourceType.SIX,
                    url='occaecati',
                ),
                entry_point='numquam',
                environment_variables={
                    "quam": 'molestiae',
                    "velit": 'error',
                },
                import_modules=[
                    shared.StorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "vitae": 'laborum',
                            "animi": 'enim',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='odit',
                        read_write=False,
                        repo='quo',
                        s3=shared.S3StorageSpec(
                            bucket='sequi',
                            checksum='tenetur',
                            endpoint='ipsam',
                            key='id',
                            region='possimus',
                            version_id='aut',
                        ),
                        source_path='quasi',
                        storage_source=shared.StorageSourceType.SIX,
                        url='temporibus',
                    ),
                ],
                parameters=[
                    'quasi',
                    'reiciendis',
                    'voluptatibus',
                ],
            ),
        ),
    ),
    signature='vero',
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

