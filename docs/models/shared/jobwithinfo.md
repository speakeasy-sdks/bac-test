# JobWithInfo


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `history`                                                                        | List[[shared.JobHistory](../../models/shared/jobhistory.md)]                     | :heavy_minus_sign:                                                               | History of changes to the job state. Not always populated in the job description |
| `job`                                                                            | [Optional[shared.Job]](../../models/shared/job.md)                               | :heavy_minus_sign:                                                               | Job info                                                                         |
| `state`                                                                          | [Optional[shared.JobState]](../../models/shared/jobstate.md)                     | :heavy_minus_sign:                                                               | The current state of the job                                                     |