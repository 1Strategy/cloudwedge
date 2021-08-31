---
title: ECS
---

## CloudWatch Configuration

When a resource is monitored it is going to be using these CloudWatch configurations to identify the metric.

| `namespace` | `dimension` | `metrics`                                                                                                                                       |
| ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS/ECS     | ClusterName | [Available CloudWatch Metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html#available_cloudwatch_metrics) |

## Service Defaults

When an alarm is created it will first review the service defaults to populate the CloudWatch alarm properties. After the service defaults, it will then apply the specific metric defaults if they are provided.

| Alarm Property         | Default Value                   |
| :--------------------- | :------------------------------ |
| **EvaluationPeriods**  | `5`                             |
| **Statistic**          | `Average`                       |
| **Period**             | `300`                           |
| **ComparisonOperator** | `GreaterThanOrEqualToThreshold` |

## Default Metrics

- `CPUUtilization`
- `MemoryUtilization`

## Supported Metrics

??? velum-metric "CPUUtilization"

    #### Metric Name

    `CPUUtilization`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | **Threshold**  | `85`          | Threshold represents a percentage of CPU |

??? velum-metric "MemoryUtilization"

    #### Metric Name

    `MemoryUtilization`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                             |
    | :------------- | :------------ | --------------------------------- |
    | **Threshold**  | `70`          | Threshold represents a percentage |

??? velum-metric "CPUReservation"

    #### Metric Name

    `CPUReservation`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | **TBD**        |               |       |

??? velum-metric "MemoryReservation"

    #### Metric Name

    `MemoryReservation`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | **TBD**        |               |       |

??? velum-metric "GPUReservation"

    #### Metric Name

    `GPUReservation`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | **TBD**        |               |       |
