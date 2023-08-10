# Job


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `api_version`                                                                                               | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         | V1beta1                                                                                                     |
| `metadata`                                                                                                  | [Optional[Metadata]](../../models/shared/metadata.md)                                                       | :heavy_minus_sign:                                                                                          | TODO this doesn't seem like it should be a part of the job as it cannot be known by a client ahead of time. |                                                                                                             |
| `spec`                                                                                                      | [Optional[Spec]](../../models/shared/spec.md)                                                               | :heavy_minus_sign:                                                                                          | The specification of this job.                                                                              |                                                                                                             |