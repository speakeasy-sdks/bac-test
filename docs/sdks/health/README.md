# health

### Available Operations

* [api_server_debug](#api_server_debug) - Returns debug information on what the current node is doing.
* [pkg_requester_publicapi_debug](#pkg_requester_publicapi_debug) - Returns debug information on what the current node is doing.

## api_server_debug

Returns debug information on what the current node is doing.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.health.api_server_debug()

if res.api_server_debug_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.APIServerDebugResponse](../../models/operations/apiserverdebugresponse.md)**


## pkg_requester_publicapi_debug

Returns debug information on what the current node is doing.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.health.pkg_requester_publicapi_debug()

if res.pkg_requester_publicapi_debug_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.PkgRequesterPublicapiDebugResponse](../../models/operations/pkgrequesterpublicapidebugresponse.md)**

