---
title: Tags
---

## CloudVelum Tags

CloudVelum is built on the pattern of tagging resources.

### Tags

??? velum-tag "cloudvelum:active"

    #### Tag Name

    ```text
    cloudvelum:active
    ```

    #### Tag Details

    |         |                 |
    | :------------ | :--------------------------|
    | **Required**    | :octicons-verified-16: |
    | **Description** | This tag controls if the resource should be included as candidate for alarms. Without this tag the cloudvelum will not identify this resource as in scope. |
    | **Default**     | No default, its either on or off |
    | **Values**      | Only the value "true" will mark the resource as in scope for alarms. Any other value will not considered. |
    | **Example**     | `true` |

??? velum-tag "cloudvelum:owner"

    #### Tag Name

    ```text
    cloudvelum:owner
    ```

    #### Tag Details

    |         |                 |
    | :------------ | :--------------------------|
    | **Required**    | :octicons-x-16: |
    | **Description** | Tag determines what owner the alerts will be marked with. You can use this owner to filter alerting methods to specifc owners. For example, you may want to receive a text just for systems you own. |
    | **Default**     | `cloudvelum` |
    | **Values**      | any string |
    | **Example**     | `customers-microservice` |

??? velum-tag "cloudvelum:level"

    #### Tag Name

    ```text
    cloudvelum:level
    ```

    #### Tag Details

    |         |                 |
    | :------------ | :--------------------------|
    | **Required**    | :octicons-x-16: |
    | **Description** | Tag determines what level the alerts will be marked as. You can use this level to filter alerting methods to specifc levels. For example, you may want to receive a text just for critical alerts. |
    | **Default**     | `medium` |
    | **Values**      | `critical` `high` `medium` `low` |
    | **Example**     | `critical` |

### Setting Metrics

??? velum-tag "cloudvelum:metrics"

    #### Tag Name

    ```text
    cloudvelum:metrics
    ```

    #### Tag Details

    |         |                 |
    | :------------ | :--------------------------|
    | **Required**    | :octicons-x-16: |
    | **Description** | Tag determines what metrics should be created for this resource. This overrides the default metrics for the service. |
    | **Default**     | Defaults to service level default metrics |
    | **Values**      | An array of supported service metrics separated with a `|` |
    | **Example**     | `CPUUtilization | DiskReadOps` |

??? velum-tag "cloudvelum:metrics:[ critical | high | medium | low ]"

    #### Tag Names

    ```text
    cloudvelum:metrics:critical
    ```

    ```text
    cloudvelum:metrics:high
    ```

    ```text
    cloudvelum:metrics:medium
    ```

    ```text
    cloudvelum:metrics:low
    ```

    #### Tag Details

    |         |                 |
    | :------------ | :--------------------------|
    | **Required**    | :octicons-x-16: |
    | **Description** | You can use these tags to separate the criticality of different metrics. Lets say you want CPUUtilization to be a `critical` metric for a given resource, but the other metrics are just `high`. You can use these tags and list the metrics for each level. |
    | **Default**     | None |
    | **Values**      | An array of supported service metrics separated with a `|` |
    | **Example**     | `CPUUtilization | DiskReadOps` |

### Alarm Overrides

??? velum-tag "cloudvelum:alarm:prop:`CloudFormationProperty`"

    #### Tag Prefix

    ```text
    cloudvelum:alarm:prop:
    ```

    #### Tag Examples

    ```text
    cloudvelum:alarm:prop:Threshold
    ```

    ```text
    cloudvelum:alarm:prop:Period
    ```

    #### Tag Details

    |                 |                                                                                                                                                                  |
    | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Required**    | :octicons-x-16:                                                                                                                                                  |
    | **Description** | Tag determines what the default property on the CloudFormation alarms will be. This is a quick way to change the property value for all metrics on the resource. |
    | **Default**     | None                                                                                                                                                             |
    | **Values**      | Refer to the [CloudFormation property documentation](../alarms/#alarm-anatomy) to see what values are valid for the property.                                  |
    | **Example**     | `cloudvelum:alarm:prop:Threshold` = `80`                                                                                                                           |

??? velum-tag "cloudvelum:alarm:metric:`MetricName`:prop:`CloudFormationProperty`"

    #### Tag Pattern

    ```text
    cloudvelum:alarm:metric:MetricName:prop:CloudFormationProperty
    ```

    #### Tag Examples

    ```text
    cloudvelum:alarm:metric:CPUUtilization:prop:Threshold
    ```

    ```text
    cloudvelum:alarm:metric:ExecutionsFailed:prop:EvaluationPeriods
    ```

    ```text
    cloudvelum:alarm:metric:ApplicationRequests3xx:prop:Period
    ```


    #### Tag Details

    |                 |                                                                                                                                 |
    | :-------------- | :------------------------------------------------------------------------------------------------------------------------------ |
    | **Required**    | :octicons-x-16:                                                                                                                 |
    | **Description** | Tag allows to target a specific metric's property and overide it with a new value.                                              |
    | **Default**     | None                                                                                                                            |
    | **Values**      | The metric must be listed as a supported metric for the service and the property must be a valid CloudFormation Alarm property. |
    | **Example**     | `cloudvelum:alarm:metric:ExecutionsFailed:prop:EvaluationPeriods` = 5                                                           |

??? info "Param: `CloudFormationProperty`"

    `CloudFormationProperty` can be replaced with valid property names in the the [Alarms](./alarms.md/#alarm-anatomy) CloudFormation template. [CloudFormation property documentation](../alarms/#alarm-anatomy)

    Examples:

    - `Threshold`
    - `EvaluationPeriods`
    - `Period`

??? info "Param: `MetricName`"

    `MetricName` can be replaced with valid metric names. [Services list](../services/)

    Examples:

    - `CPUUtilization`
    - `ExecutionsFailed`
    - `ApplicationRequests3xx`
