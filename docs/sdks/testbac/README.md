# TestBac SDK

## Overview

Bacalhau API: This page is the reference of the Bacalhau REST API. Project docs are available at https://docs.bacalhau.org/. Find more information about Bacalhau at https://github.com/bacalhau-project/bacalhau.

### Available Operations

* [api_server_approver](#api_server_approver) - Approves a job to be run on this compute node.
* [pkg_requester_publicapi_nodes](#pkg_requester_publicapi_nodes) - Displays the nodes that this requester knows about

## api_server_approver

Approves a job to be run on this compute node.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.test_bac.api_server_approver()

if res.api_server_approver_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.APIServerApproverResponse](../../models/operations/apiserverapproverresponse.md)**


## pkg_requester_publicapi_nodes

Displays the nodes that this requester knows about

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.test_bac.pkg_requester_publicapi_nodes()

if res.model_node_infos is not None:
    # handle response
```


### Response

**[operations.PkgRequesterPublicapiNodesResponse](../../models/operations/pkgrequesterpublicapinodesresponse.md)**

