# JobWithInfo


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `history`                                                                        | list[[shared.JobHistory](undefined/models/shared/jobhistory.md)]                 | :heavy_minus_sign:                                                               | History of changes to the job state. Not always populated in the job description |
| `job`                                                                            | [Optional[shared.Job]](undefined/models/shared/job.md)                           | :heavy_minus_sign:                                                               | Job info                                                                         |
| `state`                                                                          | [Optional[shared.JobState]](undefined/models/shared/jobstate.md)                 | :heavy_minus_sign:                                                               | The current state of the job                                                     |