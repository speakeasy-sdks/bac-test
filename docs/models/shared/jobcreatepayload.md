# JobCreatePayload


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `api_version`                                   | *str*                                           | :heavy_check_mark:                              | N/A                                             | V1beta1                                         |
| `client_id`                                     | *str*                                           | :heavy_check_mark:                              | the id of the client that is submitting the job |                                                 |
| `spec`                                          | [shared.Spec](../../models/shared/spec.md)      | :heavy_check_mark:                              | The specification of this job.                  |                                                 |