# RunCommandResult


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `exit_code`                                            | *Optional[int]*                                        | :heavy_minus_sign:                                     | exit code of the run.                                  |
| `runner_error`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | Runner error                                           |
| `stderr`                                               | *Optional[str]*                                        | :heavy_minus_sign:                                     | stderr of the run.                                     |
| `stderrtruncated`                                      | *Optional[bool]*                                       | :heavy_minus_sign:                                     | bool describing if stderr was truncated                |
| `stdout`                                               | *Optional[str]*                                        | :heavy_minus_sign:                                     | stdout of the run. Yaml provided for `describe` output |
| `stdouttruncated`                                      | *Optional[bool]*                                       | :heavy_minus_sign:                                     | bool describing if stdout was truncated                |