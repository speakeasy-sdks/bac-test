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
import test_bac


s = test_bac.TestBac()


res = s.api_server_approver()

if res.api_server_approver_200_application_json_string is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [TestBac SDK](docs/sdks/testbac/README.md)

* [api_server_approver](docs/sdks/testbac/README.md#api_server_approver) - Approves a job to be run on this compute node.
* [pkg_requester_publicapi_nodes](docs/sdks/testbac/README.md#pkg_requester_publicapi_nodes) - Displays the nodes that this requester knows about

### [health](docs/sdks/health/README.md)

* [api_server_debug](docs/sdks/health/README.md#api_server_debug) - Returns debug information on what the current node is doing.
* [pkg_requester_publicapi_debug](docs/sdks/health/README.md#pkg_requester_publicapi_debug) - Returns debug information on what the current node is doing.

### [job](docs/sdks/job/README.md)

* [pkg_requester_publicapi_cancel](docs/sdks/job/README.md#pkg_requester_publicapi_cancel) - Cancels the job with the job-id specified in the body payload.
* [pkg_requester_publicapi_events](docs/sdks/job/README.md#pkg_requester_publicapi_events) - Returns the events related to the job-id passed in the body payload. Useful for troubleshooting.
* [pkg_requester_publicapi_list](docs/sdks/job/README.md#pkg_requester_publicapi_list) - Simply lists jobs.
* [pkg_requester_publicapi_logs](docs/sdks/job/README.md#pkg_requester_publicapi_logs) - Displays the logs for a current job/execution
* [pkg_requester_publicapi_results](docs/sdks/job/README.md#pkg_requester_publicapi_results) - Returns the results of the job-id specified in the body payload.
* [pkg_requester_publicapi_states](docs/sdks/job/README.md#pkg_requester_publicapi_states) - Returns the state of the job-id specified in the body payload.
* [pkg_requester_publicapi_submit](docs/sdks/job/README.md#pkg_requester_publicapi_submit) - Submits a new job to the network.

### [misc](docs/sdks/misc/README.md)

* [api_server_version](docs/sdks/misc/README.md#api_server_version) - Returns the build version running on the server.

### [utils](docs/sdks/utils/README.md)

* [healthz](docs/sdks/utils/README.md#healthz)
* [id](docs/sdks/utils/README.md#id) - Returns the id of the host node.
* [livez](docs/sdks/utils/README.md#livez)
* [logz](docs/sdks/utils/README.md#logz)
* [node_info](docs/sdks/utils/README.md#node_info) - Returns the info of the node.
* [peers](docs/sdks/utils/README.md#peers) - Returns the peers connected to the host via the transport layer.
* [readyz](docs/sdks/utils/README.md#readyz)
* [varz](docs/sdks/utils/README.md#varz)
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
