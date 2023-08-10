# VersionRequest

Request must specify a `client_id`. To retrieve your `client_id`, you can do the following: (1) submit a dummy job to Bacalhau (or use one you created before), (2) run `bacalhau describe <job-id>` and fetch the `ClientID` field.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `client_id`                                                      | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              | ac13188e93c97a9c2e7cf8e86c7313156a73436036f30da1ececc2ce79f9ea51 |