# utils

### Available Operations

* [healthz](#healthz)
* [id](#id) - Returns the id of the host node.
* [livez](#livez)
* [logz](#logz)
* [node_info](#node_info) - Returns the info of the node.
* [peers](#peers) - Returns the peers connected to the host via the transport layer.
* [readyz](#readyz)
* [varz](#varz)

## healthz

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.healthz()

if res.types_health_info is not None:
    # handle response
```


### Response

**[operations.HealthzResponse](../../models/operations/healthzresponse.md)**


## id

Returns the id of the host node.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.id()

if res.id_200_text_plain_string is not None:
    # handle response
```


### Response

**[operations.IDResponse](../../models/operations/idresponse.md)**


## livez

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.livez()

if res.livez_200_text_plain_string is not None:
    # handle response
```


### Response

**[operations.LivezResponse](../../models/operations/livezresponse.md)**


## logz

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.logz()

if res.logz_200_text_plain_string is not None:
    # handle response
```


### Response

**[operations.LogzResponse](../../models/operations/logzresponse.md)**


## node_info

Returns the info of the node.

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.node_info()

if res.model_node_info is not None:
    # handle response
```


### Response

**[operations.NodeInfoResponse](../../models/operations/nodeinforesponse.md)**


## peers

As described in the [architecture docs](https://docs.bacalhau.org/about-bacalhau/architecture), each node is connected to a number of peer nodes.

Example response:
```json
{
  "bacalhau-job-event": [
    "QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL",
    "QmXaXu9N5GNetatsvwnTfQqNtSeKAD6uCmarbh3LMRYAcF",
    "QmVAb7r2pKWCuyLpYWoZr9syhhFnTWeFaByHdb8PkkhLQG",
    "QmUDAXvv31WPZ8U9CzuRTMn9iFGiopGE7rHiah1X8a6PkT",
    "QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86"
  ]
}
```

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.peers()

if res.peer_addr_infos is not None:
    # handle response
```


### Response

**[operations.PeersResponse](../../models/operations/peersresponse.md)**


## readyz

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.readyz()

if res.readyz_200_text_plain_string is not None:
    # handle response
```


### Response

**[operations.ReadyzResponse](../../models/operations/readyzresponse.md)**


## varz

### Example Usage

```python
import test_bac


s = test_bac.TestBac()


res = s.utils.varz()

if res.varz_200_application_json_integers is not None:
    # handle response
```


### Response

**[operations.VarzResponse](../../models/operations/varzresponse.md)**

