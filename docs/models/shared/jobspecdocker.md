# JobSpecDocker


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `entrypoint`                                      | list[*str*]                                       | :heavy_minus_sign:                                | optionally override the default entrypoint        |
| `environment_variables`                           | list[*str*]                                       | :heavy_minus_sign:                                | a map of env to run the container with            |
| `image`                                           | *Optional[str]*                                   | :heavy_minus_sign:                                | this should be pullable by docker                 |
| `parameters`                                      | list[*str*]                                       | :heavy_minus_sign:                                | Parameters holds additional commandline arguments |
| `working_directory`                               | *Optional[str]*                                   | :heavy_minus_sign:                                | working directory inside the container            |