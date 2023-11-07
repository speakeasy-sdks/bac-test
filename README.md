# bac-test

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/bac-test.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import bac

s = bac.Bac()


res = s.job.approve()

if res.success is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [.job](docs/sdks/job/README.md)

* [approve](docs/sdks/job/README.md#approve) - Approves a job to be run on this compute node.
* [cancel](docs/sdks/job/README.md#cancel) - Cancels the job with the job-id specified in the body payload.
* [submit](docs/sdks/job/README.md#submit) - Submits a new job to the network.

### [.debug](docs/sdks/debug/README.md)

* [get](docs/sdks/debug/README.md#get) - Returns debug information on what the current node is doing.

### [.healthz](docs/sdks/healthz/README.md)

* [get](docs/sdks/healthz/README.md#get)

### [.host_node_id](docs/sdks/hostnodeid/README.md)

* [get](docs/sdks/hostnodeid/README.md#get) - Returns the id of the host node.

### [.livez](docs/sdks/livez/README.md)

* [get](docs/sdks/livez/README.md#get)

### [.logz](docs/sdks/logz/README.md)

* [get](docs/sdks/logz/README.md#get)

### [.node_info](docs/sdks/nodeinfo/README.md)

* [get](docs/sdks/nodeinfo/README.md#get) - Returns the info of the node.

### [.connected_peers](docs/sdks/connectedpeers/README.md)

* [get](docs/sdks/connectedpeers/README.md#get) - Returns the peers connected to the host via the transport layer.

### [.readyz](docs/sdks/readyz/README.md)

* [get](docs/sdks/readyz/README.md#get)

### [.requester_debug](docs/sdks/requesterdebug/README.md)

* [get](docs/sdks/requesterdebug/README.md#get) - Returns debug information on what the current node is doing.

### [.job_events](docs/sdks/jobevents/README.md)

* [get](docs/sdks/jobevents/README.md#get) - Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.

### [.jobs](docs/sdks/jobs/README.md)

* [list](docs/sdks/jobs/README.md#list) - Simply lists jobs.

### [.job_logs](docs/sdks/joblogs/README.md)

* [display](docs/sdks/joblogs/README.md#display) - Displays the logs for a current job/execution

### [.nodes](docs/sdks/nodes/README.md)

* [display](docs/sdks/nodes/README.md#display) - Displays the nodes that this requester knows about

### [.results](docs/sdks/results/README.md)

* [get](docs/sdks/results/README.md#get) - Returns the results of the job-id specified in the body payload.

### [.states](docs/sdks/states/README.md)

* [get](docs/sdks/states/README.md#get) - Returns the state of the job-id specified in the body payload.

### [.varz](docs/sdks/varz/README.md)

* [get](docs/sdks/varz/README.md#get)

### [.build_version](docs/sdks/buildversion/README.md)

* [get](docs/sdks/buildversion/README.md#get) - Returns the build version running on the server.
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


## Example

```python
import bac

s = bac.Bac()


res = None
try:
    res = s.job.approve()

except (BadRequest) as e:
    print(e) # handle exception
except (Forbidden) as e:
    print(e) # handle exception

except (InternalServerError) as e:
    print(e) # handle exception

if res.success is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://bootstrap.production.bacalhau.org:1234/` | None |

For example:

```python
import bac

s = bac.Bac(
    server_idx=0,
)


res = s.job.approve()

if res.success is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import bac

s = bac.Bac(
    server_url="http://bootstrap.production.bacalhau.org:1234/",
)


res = s.job.approve()

if res.success is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import bac
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = bac.Bac(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
