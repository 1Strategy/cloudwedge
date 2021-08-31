---
title: Examples
---

## Example

A showcase on ways to use tags to get your desired configuration.

??? example "Monitoring resource with owner"

    #### Apply tags

    - ##### Opt-in to monitoring

        _Key_
        ```
        cloudvelum:active
        ```
        _Value_
        ```
        true
        ```

    - ##### Assign the owner

        _Key_
        ```
        cloudvelum:owner
        ```
        _Value_
        ```
        yourowner
        ```

??? example "Monitoring resource with owner and critical level"

    #### Apply tags

    - ##### Opt-in to monitoring

        _Key_
        ```
        cloudvelum:active
        ```
        _Value_
        ```
        true
        ```

    - ##### Assign the owner

        _Key_
        ```
        cloudvelum:owner
        ```
        _Value_
        ```
        yourowner
        ```

    - ##### Assign the level

        _Key_
        ```
        cloudvelum:level
        ```
        _Value_
        ```
        critical
        ```

??? example "Monitor EC2 instance with certain metrics"

    #### Apply tags

    - ##### Opt-in to monitoring

        _Key_
        ```
        cloudvelum:active
        ```
        _Value_
        ```
        true
        ```

    - ##### Assign the owner

        _Key_
        ```
        cloudvelum:owner
        ```
        _Value_
        ```
        yourowner
        ```

    - ##### Assign the metrics

        _Key_
        ```
        cloudvelum:metrics
        ```
        _Value_
        ```
        CPUUtilization | NetworkIn | NetworkOut
        ```

??? example "Monitor EC2 instance with property overrides"

    #### Apply tags

    - ##### Opt-in to monitoring

        _Key_
        ```
        cloudvelum:active
        ```
        _Value_
        ```
        true
        ```

    - ##### Assign the owner

        _Key_
        ```
        cloudvelum:owner
        ```
        _Value_
        ```
        yourowner
        ```

    - ##### Assign the property override

        _Key_
        ```
        cloudvelum:alarm:prop:Period
        ```
        _Value_
        ```
        10
        ```

    - ##### Assign the metric property override

        _Key_
        ```
        cloudvelum:alarm:metric:CPUUtilization:prop:Threshold
        ```
        _Value_
        ```
        78
        ```
