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
from bac.models import shared

s = bac.Bac()

req = shared.VersionRequest(
    client_id='ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51',
)

res = s.build_version.get(req)

if res.version_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [BuildVersion](docs/sdks/buildversion/README.md)

* [get](docs/sdks/buildversion/README.md#get) - Returns the build version running on the server.

### [ConnectedPeers](docs/sdks/connectedpeers/README.md)

* [get](docs/sdks/connectedpeers/README.md#get) - Returns the peers connected to the host via the transport layer.

### [Debug](docs/sdks/debug/README.md)

* [get](docs/sdks/debug/README.md#get) - Returns debug information on what the current node is doing.

### [Healthz](docs/sdks/healthz/README.md)

* [get](docs/sdks/healthz/README.md#get)

### [HostNodeID](docs/sdks/hostnodeid/README.md)

* [get](docs/sdks/hostnodeid/README.md#get) - Returns the id of the host node.

### [Job](docs/sdks/job/README.md)

* [approve](docs/sdks/job/README.md#approve) - Approves a job to be run on this compute node.
* [cancel](docs/sdks/job/README.md#cancel) - Cancels the job with the job-id specified in the body payload.
* [submit](docs/sdks/job/README.md#submit) - Submits a new job to the network.

### [JobEvents](docs/sdks/jobevents/README.md)

* [get](docs/sdks/jobevents/README.md#get) - Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.

### [JobLogs](docs/sdks/joblogs/README.md)

* [display](docs/sdks/joblogs/README.md#display) - Displays the logs for a current job/execution

### [Jobs](docs/sdks/jobs/README.md)

* [list](docs/sdks/jobs/README.md#list) - Simply lists jobs.

### [Livez](docs/sdks/livez/README.md)

* [get](docs/sdks/livez/README.md#get)

### [Logz](docs/sdks/logz/README.md)

* [get](docs/sdks/logz/README.md#get)

### [NodeInfo](docs/sdks/nodeinfo/README.md)

* [get](docs/sdks/nodeinfo/README.md#get) - Returns the info of the node.

### [Nodes](docs/sdks/nodes/README.md)

* [display](docs/sdks/nodes/README.md#display) - Displays the nodes that this requester knows about

### [Readyz](docs/sdks/readyz/README.md)

* [get](docs/sdks/readyz/README.md#get)

### [RequesterDebug](docs/sdks/requesterdebug/README.md)

* [get](docs/sdks/requesterdebug/README.md#get) - Returns debug information on what the current node is doing.

### [Results](docs/sdks/results/README.md)

* [get](docs/sdks/results/README.md#get) - Returns the results of the job-id specified in the body payload.

### [States](docs/sdks/states/README.md)

* [get](docs/sdks/states/README.md#get) - Returns the state of the job-id specified in the body payload.

### [Varz](docs/sdks/varz/README.md)

* [get](docs/sdks/varz/README.md#get)
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
