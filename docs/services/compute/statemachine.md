---
title: Step Functions
---

## CloudWatch Configuration

When a resource is monitored it is going to be using these CloudWatch configurations to identify the metric.

| `namespace` | `dimension`     | `metrics`                                                                                                      |
| ----------- | --------------- | -------------------------------------------------------------------------------------------------------------- |
| AWS/States  | StateMachineArn | [Available CloudWatch Metrics](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-cw-metrics.html) |

## Service Defaults

When an alarm is created it will first review the service defaults to populate the CloudWatch alarm properties. After the service defaults, it will then apply the specific metric defaults if they are provided.

| Alarm Property | Default Value |
| :------------- | :------------ |
| **Statistic**  | `Sum`         |

## Default Metrics

- `ExecutionsFailed`
- `ExecutionThrottled`
- `ExecutionTime`

## Supported Metrics

??? velum-metric "ExecutionsStarted"

    #### Metric Name

    `ExecutionsStarted`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionThrottled"

    #### Metric Name

    `ExecutionThrottled`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionsAborted"

    #### Metric Name

    `ExecutionsAborted`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionsSucceeded"

    #### Metric Name

    `ExecutionsSucceeded`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionsFailed"

    #### Metric Name

    `ExecutionsFailed`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionsTimedOut"

    #### Metric Name

    `ExecutionsTimedOut`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "ExecutionTime"

    #### Metric Name

    `ExecutionTime`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |
