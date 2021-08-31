---
title: AutoScaling
---

## CloudWatch Configuration

When a resource is monitored it is going to be using these CloudWatch configurations to identify the metric.

| `namespace` | `dimension` | `metrics`                                                                                                                                       |
| ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS/EC2     | AutoScalingGroupName  | [Available CloudWatch Metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics) |

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
- `NetworkIn`
- `NetworkOut`

## Supported Metrics

??? velum-metric "CPUUtilization"

    #### Metric Name

    `CPUUtilization`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | **Threshold**  | `85`          | Threshold represents a percentage of CPU |

??? velum-metric "StatusCheckFailed_Instance"

    #### Metric Name

    `StatusCheckFailed_Instance`

    #### Metric Defaults

    | Alarm Property        | Default Value | Notes                        |
    | :-------------------- | :------------ | ---------------------------- |
    | **Threshold**         | `1`           | This is a count of failures. |
    | **EvaluationPeriods** | `3`           |                              |

??? velum-metric "StatusCheckFailed_System"

    #### Metric Name

    `StatusCheckFailed_System`

    #### Metric Defaults

    | Alarm Property        | Default Value | Notes                        |
    | :-------------------- | :------------ | ---------------------------- |
    | **Threshold**         | `1`           | This is a count of failures. |
    | **EvaluationPeriods** | `2`           |                              |

??? velum-metric "DiskReadOps"

    #### Metric Name

    `DiskReadOps`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes  |
    | :------------- | :------------ | ------ |
    | **Threshold**  | `5000`        | Count |

??? velum-metric "DiskWriteOps"

    #### Metric Name

    `DiskWriteOps`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes  |
    | :------------- | :------------ | ------ |
    | **Threshold**  | `5000`        | Count |

??? velum-metric "NetworkIn"

    #### Metric Name

    `NetworkIn`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes  |
    | :------------- | :------------ | ------ |
    | **Threshold**  | `1000000`        | Count |

??? velum-metric "NetworkOut"

    #### Metric Name

    `NetworkOut`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes  |
    | :------------- | :------------ | ------ |
    | **Threshold**  | `1000000`        | Count |
