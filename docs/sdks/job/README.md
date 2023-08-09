# job

### Available Operations

* [pkg_requester_publicapi_cancel](#pkg_requester_publicapi_cancel) - Cancels the job with the job-id specified in the body payload.
* [pkg_requester_publicapi_events](#pkg_requester_publicapi_events) - Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.
* [pkg_requester_publicapi_list](#pkg_requester_publicapi_list) - Simply lists jobs.
* [pkg_requester_publicapi_logs](#pkg_requester_publicapi_logs) - Displays the logs for a current job/execution
* [pkg_requester_publicapi_results](#pkg_requester_publicapi_results) - Returns the results of the job-id specified in the body payload.
* [pkg_requester_publicapi_states](#pkg_requester_publicapi_states) - Returns the state of the job-id specified in the body payload.
* [pkg_requester_publicapi_submit](#pkg_requester_publicapi_submit) - Submits a new job to the network.

## pkg_requester_publicapi_cancel

Cancels a job specified by `id` as long as that job belongs to `client_id`.

Returns the current jobstate after the cancel request has been processed.

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiCancelRequest(
    client_public_key='corrupti',
    payload=shared.ModelJobCancelPayload(
        client_id='provident',
        job_id='distinctio',
        reason='quibusdam',
    ),
    signature='unde',
)

res = s.job.pkg_requester_publicapi_cancel(req)

if res.publicapi_cancel_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.PublicapiCancelRequest](../../models/shared/publicapicancelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PkgRequesterPublicapiCancelResponse](../../models/operations/pkgrequesterpublicapicancelresponse.md)**


## pkg_requester_publicapi_events

Events (e.g. Created, Bid, BidAccepted, ..., ResultsAccepted, ResultsPublished) are useful to track the progress of a job.


### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiEventsRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    filters=shared.PublicapiEventFilterOptions(
        exclude_execution_level=False,
        exclude_job_level=False,
        since=857946,
    ),
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.job.pkg_requester_publicapi_events(req)

if res.publicapi_events_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.PublicapiEventsRequest](../../models/shared/publicapieventsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PkgRequesterPublicapiEventsResponse](../../models/operations/pkgrequesterpublicapieventsresponse.md)**


## pkg_requester_publicapi_list

Returns the first (sorted) #`max_jobs` jobs that belong to the `client_id` passed in the body payload (by default).
If `return_all` is set to true, it returns all jobs on the Bacalhau network.

If `id` is set, it returns only the job with that ID.

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiListRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    exclude_tags=[
        'illum',
        'vel',
        'error',
    ],
    id='9304c616-291f-41ad-b862-54e133c0149e',
    include_tags=[
        'suscipit',
        'iure',
        'magnam',
    ],
    max_jobs=10,
    return_all=False,
    sort_by='created_at',
    sort_reverse=False,
)

res = s.job.pkg_requester_publicapi_list(req)

if res.publicapi_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.PublicapiListRequest](../../models/shared/publicapilistrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PkgRequesterPublicapiListResponse](../../models/operations/pkgrequesterpublicapilistresponse.md)**


## pkg_requester_publicapi_logs

Shows the output from the job specified by `id` as long as that job belongs to `client_id`.

The ouput will be continuous until either, the client disconnects or the execution completes.

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiLogRequest(
    client_public_key='debitis',
    payload=shared.ModelLogsPayload(
        client_id='ipsa',
        execution_id='delectus',
        follow=False,
        job_id='tempora',
        with_history=False,
    ),
    signature='suscipit',
)

res = s.job.pkg_requester_publicapi_logs(req)

if res.pkg_requester_publicapi_logs_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.PublicapiLogRequest](../../models/shared/publicapilogrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PkgRequesterPublicapiLogsResponse](../../models/operations/pkgrequesterpublicapilogsresponse.md)**


## pkg_requester_publicapi_results

Example response:

```json
{
  "results": [
    {
      "NodeID": "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
      "Data": {
        "StorageSource": "IPFS",
        "Name": "job-9304c616-291f-41ad-b862-54e133c0149e-shard-0-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
        "CID": "QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe"
      }
    }
  ]
}
```

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiStateRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.job.pkg_requester_publicapi_results(req)

if res.publicapi_results_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.PublicapiStateRequest](../../models/shared/publicapistaterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.PkgRequesterPublicapiResultsResponse](../../models/operations/pkgrequesterpublicapiresultsresponse.md)**


## pkg_requester_publicapi_states

Example response:

```json
{
  "state": {
    "Nodes": {
      "QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86": {
        "Shards": {
          "0": {
            "NodeId": "QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86",
            "State": "Cancelled",
            "VerificationResult": {},
            "PublishedResults": {}
          }
        }
      },
      "QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3": {
        "Shards": {
          "0": {
            "NodeId": "QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3",
            "State": "Cancelled",
            "VerificationResult": {},
            "PublishedResults": {}
          }
        }
      },
      "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL": {
        "Shards": {
          "0": {
            "NodeId": "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
            "State": "Completed",
            "Status": "Got results proposal of length: 0",
            "VerificationResult": {
              "Complete": true,
              "Result": true
            },
            "PublishedResults": {
              "StorageSource": "IPFS",
              "Name": "job-9304c616-291f-41ad-b862-54e133c0149e-shard-0-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
              "CID": "QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe"
            },
            "RunOutput": {
              "stdout": "Thu Nov 17 13:32:55 UTC 2022\n",
              "stdouttruncated": false,
              "stderr": "",
              "stderrtruncated": false,
              "exitCode": 0,
              "runnerError": ""
            }
          }
        }
      }
    }
  }
}
```

### Example Usage

```python
import test_bac
from test_bac.models import shared

s = test_bac.TestBac()

req = shared.PublicapiStateRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
    job_id='9304c616-291f-41ad-b862-54e133c0149e',
)

res = s.job.pkg_requester_publicapi_states(req)

if res.publicapi_state_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.PublicapiStateRequest](../../models/shared/publicapistaterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.PkgRequesterPublicapiStatesResponse](../../models/operations/pkgrequesterpublicapistatesresponse.md)**


## pkg_requester_publicapi_submit

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

req = shared.PublicapiSubmitRequest(
    client_public_key='molestiae',
    payload=shared.ModelJobCreatePayload(
        api_version='V1beta1',
        client_id='minus',
        spec=shared.ModelSpec(
            annotations=[
                'voluptatum',
                'iusto',
                'excepturi',
                'nisi',
            ],
            deal=shared.ModelDeal(
                concurrency=925597,
                targeting_mode=False,
            ),
            do_not_track=False,
            docker=shared.ModelJobSpecDocker(
                entrypoint=[
                    'ab',
                    'quis',
                    'veritatis',
                    'deserunt',
                ],
                environment_variables=[
                    'ipsam',
                ],
                image='repellendus',
                parameters=[
                    'quo',
                    'odit',
                    'at',
                    'at',
                ],
                working_directory='maiores',
            ),
            engine=shared.ModelEngine.TWO,
            inputs=[
                shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "esse": 'totam',
                        "porro": 'dolorum',
                        "dicta": 'nam',
                        "officia": 'occaecati',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='fugit',
                    read_write=False,
                    repo='deleniti',
                    s3=shared.ModelS3StorageSpec(
                        bucket='hic',
                        checksum='optio',
                        endpoint='totam',
                        key='beatae',
                        region='commodi',
                        version_id='molestiae',
                    ),
                    source_path='modi',
                    storage_source=shared.ModelStorageSourceType.ONE,
                    url='impedit',
                ),
                shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "esse": 'ipsum',
                        "excepturi": 'aspernatur',
                        "perferendis": 'ad',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='natus',
                    read_write=False,
                    repo='sed',
                    s3=shared.ModelS3StorageSpec(
                        bucket='iste',
                        checksum='dolor',
                        endpoint='natus',
                        key='laboriosam',
                        region='hic',
                        version_id='saepe',
                    ),
                    source_path='fuga',
                    storage_source=shared.ModelStorageSourceType.FOUR,
                    url='corporis',
                ),
                shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "iure": 'saepe',
                        "quidem": 'architecto',
                        "ipsa": 'reiciendis',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='est',
                    read_write=False,
                    repo='mollitia',
                    s3=shared.ModelS3StorageSpec(
                        bucket='laborum',
                        checksum='dolores',
                        endpoint='dolorem',
                        key='corporis',
                        region='explicabo',
                        version_id='nobis',
                    ),
                    source_path='enim',
                    storage_source=shared.ModelStorageSourceType.SIX,
                    url='nemo',
                ),
                shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "excepturi": 'accusantium',
                        "iure": 'culpa',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='doloribus',
                    read_write=False,
                    repo='sapiente',
                    s3=shared.ModelS3StorageSpec(
                        bucket='architecto',
                        checksum='mollitia',
                        endpoint='dolorem',
                        key='culpa',
                        region='consequuntur',
                        version_id='repellat',
                    ),
                    source_path='mollitia',
                    storage_source=shared.ModelStorageSourceType.FIVE,
                    url='numquam',
                ),
            ],
            network=shared.ModelNetworkConfig(
                domains=[
                    'quam',
                    'molestiae',
                ],
                type=shared.ModelNetwork.ZERO,
            ),
            node_selectors=[
                shared.ModelLabelSelectorRequirement(
                    key='quia',
                    operator=shared.SelectionOperator.IN,
                    values=[
                        'laborum',
                    ],
                ),
                shared.ModelLabelSelectorRequirement(
                    key='animi',
                    operator=shared.SelectionOperator.EQUAL_EQUAL_,
                    values=[
                        'quo',
                    ],
                ),
                shared.ModelLabelSelectorRequirement(
                    key='sequi',
                    operator=shared.SelectionOperator.LT,
                    values=[
                        'id',
                        'possimus',
                    ],
                ),
            ],
            outputs=[
                shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "error": 'temporibus',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='laborum',
                    read_write=False,
                    repo='quasi',
                    s3=shared.ModelS3StorageSpec(
                        bucket='reiciendis',
                        checksum='voluptatibus',
                        endpoint='vero',
                        key='nihil',
                        region='praesentium',
                        version_id='voluptatibus',
                    ),
                    source_path='ipsa',
                    storage_source=shared.ModelStorageSourceType.SIX,
                    url='voluptate',
                ),
            ],
            publisher=shared.ModelPublisher.FOUR,
            publisher_spec=shared.ModelPublisherSpec(
                params={
                    "doloremque": 'reprehenderit',
                },
                type=shared.ModelPublisher.ONE,
            ),
            resources=shared.ModelResourceUsageConfig(
                cpu='maiores',
                disk='dicta',
                gpu='corporis',
                memory='dolore',
            ),
            timeout=480894,
            wasm=shared.ModelJobSpecWasm(
                entry_module=shared.ModelStorageSpec(
                    cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                    metadata={
                        "harum": 'enim',
                    },
                    name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                    path='accusamus',
                    read_write=False,
                    repo='commodi',
                    s3=shared.ModelS3StorageSpec(
                        bucket='repudiandae',
                        checksum='quae',
                        endpoint='ipsum',
                        key='quidem',
                        region='molestias',
                        version_id='excepturi',
                    ),
                    source_path='pariatur',
                    storage_source=shared.ModelStorageSourceType.TWO,
                    url='praesentium',
                ),
                entry_point='rem',
                environment_variables={
                    "quasi": 'repudiandae',
                    "sint": 'veritatis',
                    "itaque": 'incidunt',
                    "enim": 'consequatur',
                },
                import_modules=[
                    shared.ModelStorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "explicabo": 'deserunt',
                            "distinctio": 'quibusdam',
                            "labore": 'modi',
                            "qui": 'aliquid',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='cupiditate',
                        read_write=False,
                        repo='quos',
                        s3=shared.ModelS3StorageSpec(
                            bucket='perferendis',
                            checksum='magni',
                            endpoint='assumenda',
                            key='ipsam',
                            region='alias',
                            version_id='fugit',
                        ),
                        source_path='dolorum',
                        storage_source=shared.ModelStorageSourceType.FIVE,
                        url='tempora',
                    ),
                    shared.ModelStorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "tempore": 'labore',
                            "delectus": 'eum',
                            "non": 'eligendi',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='sint',
                        read_write=False,
                        repo='aliquid',
                        s3=shared.ModelS3StorageSpec(
                            bucket='provident',
                            checksum='necessitatibus',
                            endpoint='sint',
                            key='officia',
                            region='dolor',
                            version_id='debitis',
                        ),
                        source_path='a',
                        storage_source=shared.ModelStorageSourceType.SIX,
                        url='in',
                    ),
                    shared.ModelStorageSpec(
                        cid='QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe',
                        metadata={
                            "illum": 'maiores',
                            "rerum": 'dicta',
                        },
                        name='job-9304c616-291f-41ad-b862-54e133c0149e-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL',
                        path='magnam',
                        read_write=False,
                        repo='cumque',
                        s3=shared.ModelS3StorageSpec(
                            bucket='facere',
                            checksum='ea',
                            endpoint='aliquid',
                            key='laborum',
                            region='accusamus',
                            version_id='non',
                        ),
                        source_path='occaecati',
                        storage_source=shared.ModelStorageSourceType.THREE,
                        url='accusamus',
                    ),
                ],
                parameters=[
                    'quidem',
                    'provident',
                    'nam',
                    'id',
                ],
            ),
        ),
    ),
    signature='blanditiis',
)

res = s.job.pkg_requester_publicapi_submit(req)

if res.publicapi_submit_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.PublicapiSubmitRequest](../../models/shared/publicapisubmitrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PkgRequesterPublicapiSubmitResponse](../../models/operations/pkgrequesterpublicapisubmitresponse.md)**

