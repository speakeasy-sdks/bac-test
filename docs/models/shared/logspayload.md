# LogsPayload


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `client_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | the id of the client that is requesting the logs                     |
| `execution_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | the execution to be shown                                            |
| `job_id`                                                             | *str*                                                                | :heavy_check_mark:                                                   | the job id of the job to be shown                                    |
| `follow`                                                             | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | whether the logs should be followed after the current logs are shown |
| `with_history`                                                       | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | whether the logs history is required                                 |