# CancelRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `client_public_key`                                                | *str*                                                              | :heavy_check_mark:                                                 | The base64-encoded public key of the client:                       |
| `payload`                                                          | [shared.JobCancelPayload](../../models/shared/jobcancelpayload.md) | :heavy_check_mark:                                                 | The data needed to cancel a running job on the network             |
| `signature`                                                        | *str*                                                              | :heavy_check_mark:                                                 | A base64-encoded signature of the data, signed by the client:      |