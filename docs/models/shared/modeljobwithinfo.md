# ModelJobWithInfo


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `history`                                                                        | list[[ModelJobHistory](../../models/shared/modeljobhistory.md)]                  | :heavy_minus_sign:                                                               | History of changes to the job state. Not always populated in the job description |
| `job`                                                                            | [Optional[ModelJob]](../../models/shared/modeljob.md)                            | :heavy_minus_sign:                                                               | Job info                                                                         |
| `state`                                                                          | [Optional[ModelJobState]](../../models/shared/modeljobstate.md)                  | :heavy_minus_sign:                                                               | The current state of the job                                                     |