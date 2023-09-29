# JobCreatePayload


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `api_version`                                            | *Optional[str]*                                          | :heavy_check_mark:                                       | N/A                                                      | V1beta1                                                  |
| `client_id`                                              | *Optional[str]*                                          | :heavy_check_mark:                                       | the id of the client that is submitting the job          |                                                          |
| `spec`                                                   | [Optional[shared.Spec]](undefined/models/shared/spec.md) | :heavy_check_mark:                                       | The specification of this job.                           |                                                          |