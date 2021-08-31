---
title: Alarms
---

## CloudWatch

CloudWatch is an umbrella for a few different features. The one CloudVelum is using heavily is the CloudWatch Alarms features.

CloudWatch Alarms are basically a way to set some configurations around a provided metric. CloudWatch will then monitor that metric and when certain thresholds are met based on your configuration it will send an alert out.

!!! info "CloudWatch Concepts"

    Jump into the documentation to learn more about the main concepts with CloudWatch.

    [CloudWatch Core Concepts :octicons-link-external-16:](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)


    A few notable terms to learn:

    - `namespace` [:octicons-link-external-16:](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace)

    - `dimension` [:octicons-link-external-16:](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension)

    - `metrics` [:octicons-link-external-16:](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric)

## Alarm Anatomy

CloudVelum uses CloudFormation to create the alarms for any given resource. The CloudFormation documentation is helpful to get oriented around what information goes into building an alarm.

The highlighted properties are the one CloudVelum exposes and you can manipulate for any resource with tags.

```yaml linenums="1" hl_lines="9 14 24 25 26 28"
CloudVelumAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
        ActionsEnabled: Boolean
        AlarmActions:
            - String
        AlarmDescription: String
        AlarmName: String
        ComparisonOperator: String
        DatapointsToAlarm: Integer
        Dimensions:
            - Dimension
        EvaluateLowSampleCountPercentile: String
        EvaluationPeriods: Integer
        ExtendedStatistic: String
        InsufficientDataActions:
            - String
        MetricName: String
        Metrics:
            - MetricDataQuery
        Namespace: String
        OKActions:
            - String
        Period: Integer
        Statistic: String
        Threshold: Double
        ThresholdMetricId: String
        TreatMissingData: String
        Unit: String
```
