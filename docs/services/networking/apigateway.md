---
title: API Gateway
---

## CloudWatch Configuration

When a resource is monitored it is going to be using these CloudWatch configurations to identify the metric.

| `namespace`    | `dimension`     | `metrics`                                                                                                                            |
| -------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| AWS/ApiGateway | EnvironmentName | [Available CloudWatch Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html) |

## Service Defaults

When an alarm is created it will first review the service defaults to populate the CloudWatch alarm properties. After the service defaults, it will then apply the specific metric defaults if they are provided.

| Alarm Property | Default Value |
| :------------- | :------------ |
| **Statistic**  | `Sum` |

## Default Metrics

- `Latency`
- `IntegrationLatency`
- `5XXError`
- `4XXError`

## Supported Metrics

??? velum-metric "Latency"

    #### Metric Name

    `Latency`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "IntegrationLatency"

    #### Metric Name

    `IntegrationLatency`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "5XXError"

    #### Metric Name

    `5XXError`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |

??? velum-metric "4XXError"

    #### Metric Name

    `4XXError`

    #### Metric Defaults

    | Alarm Property | Default Value | Notes |
    | :------------- | :------------ | ----- |
    | TBD            |               |       |