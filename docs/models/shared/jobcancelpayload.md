# JobCancelPayload


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `client_id`                                     | *Optional[str]*                                 | :heavy_check_mark:                              | the id of the client that is submitting the job |
| `job_id`                                        | *Optional[str]*                                 | :heavy_check_mark:                              | the job id of the job to be canceled            |
| `reason`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | The reason that the job is being canceled       |