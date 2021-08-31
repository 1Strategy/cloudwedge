---
title: ElasticBeanstalk
---

## CloudWatch Configuration

When a resource is monitored it is going to be using these CloudWatch configurations to identify the metric.

| `namespace` | `dimension` | `metrics`                                                                                                                                       |
| ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS/ElasticBeanstalk     | EnvironmentName  | [Available CloudWatch Metrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-cloudwatch.html#health-enhanced-cloudwatch-metrics) |

## Service Defaults

When an alarm is created it will first review the service defaults to populate the CloudWatch alarm properties. After the service defaults, it will then apply the specific metric defaults if they are provided.

| Alarm Property         | Default Value                   |
| :--------------------- | :------------------------------ |
| **Statistic**          | `Average`                       |

## Default Metrics

- `ApplicationRequests2xx`
- `ApplicationRequests3xx`
- `ApplicationRequests4xx`
- `ApplicationRequests5xx`

## Supported Metrics

??? velum-metric "ApplicationRequests2xx"

    #### Metric Name

    `ApplicationRequests2xx`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | TBD  |           |  |

??? velum-metric "ApplicationRequests3xx"

    #### Metric Name

    `ApplicationRequests3xx`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | TBD  |           |  |

??? velum-metric "ApplicationRequests4xx"

    #### Metric Name

    `ApplicationRequests4xx`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | TBD  |           |  |

??? velum-metric "ApplicationRequests5xx"

    #### Metric Name

    `ApplicationRequests5xx`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes                                    |
    | :------------- | :------------ | ---------------------------------------- |
    | TBD  |           |  |
