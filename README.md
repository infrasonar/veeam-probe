[![CI](https://github.com/infrasonar/veeam-probe/workflows/CI/badge.svg)](https://github.com/infrasonar/veeam-probe/actions)
[![Release Version](https://img.shields.io/github/release/infrasonar/veeam-probe)](https://github.com/infrasonar/veeam-probe/releases)

# InfraSonar Veeam Probe

Documentation: https://docs.infrasonar.com/collectors/probes/veeam/

## Environment variable

Variable            | Default                        | Description
------------------- | ------------------------------ | ------------
`AGENTCORE_HOST`    | `127.0.0.1`                    | Hostname or Ip address of the AgentCore.
`AGENTCORE_PORT`    | `8750`                         | AgentCore port to connect to.
`INFRASONAR_CONF`   | `/data/config/infrasonar.yaml` | File with probe and asset configuration like credentials.
`MAX_PACKAGE_SIZE`  | `500`                          | Maximum package size in kilobytes _(1..2000)_.
`MAX_CHECK_TIMEOUT` | `300`                          | Check time-out is 80% of the interval time with `MAX_CHECK_TIMEOUT` in seconds as absolute maximum.
`DRY_RUN`           | _none_                         | Do not run demonized, just return checks and assets specified in the given yaml _(see the [Dry run section](#dry-run) below)_.
`LOG_LEVEL`         | `warning`                      | Log level (`debug`, `info`, `warning`, `error` or `critical`).
`LOG_COLORIZED`     | `0`                            | Log using colors (`0`=disabled, `1`=enabled).
`LOG_FMT`           | `%y%m%d %H:%M:%S`              | Log format prefix.

## Config

Only Grant Type `password` is currently supported.

```yaml
veeam:
  config:
    grantType: password
    clientId: 01234567-0123-0123-0123-0123456789ab
    secret: xxxxxxxxxxx
    username: my_user_name
    password: xxxxxxxxxxxx
    disableAntiforgeryToken: true
```

## Docker build

```
docker build -t veeam-probe . --no-cache
```

## Dry run

Available checks:
- `health`
- `jobs`

Create a yaml file, for example _(test.yaml)_:

```yaml
asset:
  name: "backup.foo.local"
  check: "health"
  config:
    verifySSL: false
    port: 4443
    apiVersion: v8
```

Run the probe with the `DRY_RUN` environment variable set the the yaml file above.

```
DRY_RUN=test.yaml python main.py
```
