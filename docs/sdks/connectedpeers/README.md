# ConnectedPeers
(*connected_peers*)

### Available Operations

* [get](#get) - Returns the peers connected to the host via the transport layer.

## get

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
import bac

s = bac.Bac()


res = s.connected_peers.get()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetConnectedPeersResponse](../../models/operations/getconnectedpeersresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
