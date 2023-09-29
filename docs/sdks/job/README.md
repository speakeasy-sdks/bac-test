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
    client_public_key='Industrial',
    payload=shared.JobCancelPayload(
        client_id='AI East',
        job_id='Northwest',
        reason='Jersey purple',
    ),
    signature='climax Bike',
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
    client_public_key='female grey Pound',
    payload=shared.JobCreatePayload(
        api_version='V1beta1',
        client_id='weber Thallium pish',
        spec=shared.Spec(
            annotations=[
                'Dollar',
            ],
            deal=shared.Deal(
                concurrency=264695,
                targeting_mode=False,
            ),
            do_not_track=False,
            docker=shared.JobSpecDocker(
                entrypoint=[
                    'alias',
                ],
                environment_variables=[
                    'justly',
                ],
                image='https://loremflickr.com/640/480',
                parameters=[
                    'TLS',
                ],
                working_directory='furthermore',
            ),
            engine=shared.Engine.ENGINE_DONE,
            inputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "qui": 'louse',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='/usr/lib',
                    read_write=False,
                    repo='Neodymium',
                    s3=shared.S3StorageSpec(
                        bucket='blue North lavender',
                        checksum='intranet',
                        endpoint='Chair feisty',
                        key='<key>',
                        region='temporibus pink',
                        version_id='jovially circuit',
                    ),
                    source_path='utilisation Directives',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_REPO_CLONE,
                    url='http://essential-accident.com',
                ),
            ],
            network=shared.NetworkConfig(
                domains=[
                    'Nora',
                ],
                type=shared.Network.NETWORK_NONE,
            ),
            node_selectors=[
                shared.LabelSelectorRequirement(
                    key='<key>',
                    operator=shared.SelectionOperator.NOT_EQUALS,
                    values=[
                        'Park',
                    ],
                ),
            ],
            outputs=[
                shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "recusandae": 'Kansas',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='/var/spool',
                    read_write=False,
                    repo='chaplain',
                    s3=shared.S3StorageSpec(
                        bucket='floss Creative Washington',
                        checksum='tractor',
                        endpoint='Shoes male gee',
                        key='<key>',
                        region='North',
                        version_id='EXE Diesel',
                    ),
                    source_path='Hybrid quantify failing',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_INLINE,
                    url='https://ample-boycott.name',
                ),
            ],
            publisher=shared.Publisher.PUBLISHER_UNKNOWN,
            publisher_spec=shared.PublisherSpec(
                params={
                    "ullam": 'Bahamian',
                },
                type=shared.Publisher.PUBLISHER_IPFS,
            ),
            resources=shared.ResourceUsageConfig(
                cpu='Accounts Funk',
                disk='Minivan SUV grey',
                gpu='Diesel legalise',
                memory='embrace whoever Awesome',
            ),
            timeout=13332,
            wasm=shared.JobSpecWasm(
                entry_module=shared.StorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "mollitia": 'Cargo',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='/selinux',
                    read_write=False,
                    repo='JSON Investor Colorado',
                    s3=shared.S3StorageSpec(
                        bucket='whereas exactly',
                        checksum='transmitter Renton Kids',
                        endpoint='Representative',
                        key='<key>',
                        region='Bespoke Tuna Assistant',
                        version_id='RAM West East',
                    ),
                    source_path='Tools wealthy',
                    storage_source=shared.StorageSourceType.STORAGE_SOURCE_REPO_CLONE,
                    url='http://offbeat-eyeglasses.net',
                ),
                entry_point='Bicycle throughput',
                environment_variables={
                    "enim": 'Implementation',
                },
                import_modules=[
                    shared.StorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "natus": 'card',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='/private/var',
                        read_write=False,
                        repo='Northwest monitoring',
                        s3=shared.S3StorageSpec(
                            bucket='North',
                            checksum='Hills taut',
                            endpoint='wireless state engage',
                            key='<key>',
                            region='error Turkey Bedfordshire',
                            version_id='Representative',
                        ),
                        source_path='bandwidth Analyst orchid',
                        storage_source=shared.StorageSourceType.STORAGE_SOURCE_IPFS,
                        url='http://zealous-safeguard.info',
                    ),
                ],
                parameters=[
                    'fooey',
                ],
            ),
        ),
    ),
    signature='fooey',
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

