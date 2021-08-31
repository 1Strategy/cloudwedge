import math
from abc import abstractmethod
from os import environ
from typing import Any, Dict, List, Optional, TypedDict

import boto3

from cloudvelum.utils.logger import get_logger

REGION = environ.get('REGION')

LOGGER = get_logger("cloudvelum.models")

class AWSTag(TypedDict):
    Key: str
    Value: str


class AWSResource(TypedDict):
    service: str
    name: str
    uniqueId: str
    cloudwatchDimensionId: str
    owner: str
    tags: List[AWSTag]

# class AWSResource(object):
#     service: str
#     name: str
#     uniqueId: str
#     owner: str
#     tags: List[AWSTag]

#     def __init__(self, service, name, uniqueId, owner, tags):
#         self.service = service
#         self.name = name
#         self.uniqueId = uniqueId
#         self.owner = owner
#         self.tags = tags


class AWSService():
    # Properties that the extending service needs to implement
    name: str
    default_metrics: str
    cloudwatch_namespace: str
    cloudwatch_dimension: str
    cloudwatch_dashboard_section_title: str
    default_metrics: Dict[str, Dict[str, str]]
    default_alarm_props: Dict[str, str]
    supported_metrics: Dict[str, Dict[str, str]]
    dashboard_additions: Dict[str, Any]

    # CloudVelum root tags
    TAG_ACTIVE: Optional[str] = "cloudvelum:active"
    TAG_OWNER: Optional[str] = "cloudvelum:owner"
    TAG_LEVEL: Optional[str] = "cloudvelum:level"
    # CloudVelum metrics tags
    TAG_METRICS: str = "cloudvelum:metrics"
    TAG_METRICS_CRITICAL: str = "cloudvelum:metrics:critical"
    TAG_METRICS_HIGH: str = "cloudvelum:metrics:high"
    TAG_METRICS_MEDIUM: str = "cloudvelum:metrics:medium"
    TAG_METRICS_LOW: str = "cloudvelum:metrics:low"
    # CloudVelum alarm tags
    TAG_ALARM_PROP_PREFIX: str = "cloudvelum:alarm:prop:"
    TAG_ALARM_METRIC_PREFIX: str = "cloudvelum:alarm:metric:"
    # CloudVelum stack tags
    TAG_STACK_ID_KEY: str = "cloudvelum:stack"
    TAG_STACK_ID_VALUE: str = "true"
    TAG_STACK_TYPE_KEY: str = "cloudvelum:type"

    # Defaults
    DEFAULT_OWNER: str = "cloudvelum"
    DEFAULT_LEVEL: str = "medium"
    SUPPORTED_ALERT_LEVELS: List[str] = ["critical", "high", "medium", "low"]
    SUPPORTED_ALARM_PROPS: List[str] = [
        "Statistic", "Period", "TreatMissingData", "EvaluationPeriods", "Threshold", "ComparisonOperator"]
    ALARM_TARGET_SNS: str = environ.get("ALARM_ACTION_TARGET_TOPIC_ARN")
    USER_TARGET_SNS: str = environ.get("USER_TARGET_TOPIC_ARN")

    # Alarm Description keys
    # these are used to create the alarm description e.g. Resource=1s-dustin-stress Metric=CPUUtilization Level=medium Type=AWS/EC2 Owner=cloudvelum
    ALARM_DESCRIPTION_KEY_RESOURCE: str = "Resource"
    ALARM_DESCRIPTION_KEY_METRIC: str = "Metric"
    ALARM_DESCRIPTION_KEY_LEVEL: str = "Level"
    ALARM_DESCRIPTION_KEY_OWNER: str = "Owner"
    ALARM_DESCRIPTION_KEY_TYPE: str = "Type"


    @abstractmethod
    def get_resources(session: boto3.session.Session) -> List[AWSResource]:
        raise NotImplementedError

    @abstractmethod
    def get_default_resource_alarm_props(resource: AWSResource) -> Dict[str, str]:
        # The services can override this function if need to add in defaults
        return {}

    @abstractmethod
    def build_dashboard_widgets(resources: List[AWSResource]):
        raise NotImplementedError

    @staticmethod
    def _roundup(value: int, multiple: int = 60):
        return int(math.ceil(value / multiple)) * multiple

    def validate_prop_period(value: str, resource: Optional[AWSResource]) -> str:
        """Validate the Period property"""

        validated_prop = None

        # Check it is 10, 30 or multiple of 60
        # https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html


        # Convert to int
        try:
            value_as_int = int(value)

            # Only a period greater than 60s is supported for metrics in the "AWS/" namespaces
            # # If less than 10, round up to 10
            # if value_as_int <= 10:
            #     validated_prop = "10"
            # # If less than 30, round up to 30
            # if value_as_int <= 30:
            #     validated_prop = "30"
            # Check its a multiple of 60
            if not value_as_int%60 == 0:
                # Round up to next 60
                validated_prop = AWSService._roundup(value=value_as_int, multiple=60)
            else:
                # Value is fine
                validated_prop = value

        except Exception as err:
            LOGGER.info(
                "Period property is invalid, falling back to service default")
            raise err

        return str(validated_prop)

    @staticmethod
    def build_dashboard_widgets(service, resources: List[AWSResource], widgets: Optional[Dict[str, str]] = None) -> List[Any]:
        """
        Build dashboard widgets for the resources
        """

        dashboard_widgets = []

        # Name of the service
        widget_name = {
            'type': 'text',
            'width': 24,
            'height': 1,
            'properties': {
                    'markdown': f'### **{service.cloudwatch_dashboard_section_title} Resources**'
            }
        }
        dashboard_widgets.append(widget_name)


        # If widgets are provided, use them
        if widgets:
            dashboard_widgets.extend(widgets)

        # else provide the default widgets
        else:

            # Create graph for each of the default metrics
            for metric in service.default_metrics:

                # Get resources in a block
                block = []
                after_first = False
                for resource in resources:

                    if after_first:
                        # [ "...", "ExecutionsFailed", "StateMachineArn", "arn:aws:states:us-west-2:ACCOUNTID:stateMachine:CloudVelumBuilderStateMachine-Xm2QclLByXty" ]
                        block.append(['...', resource['cloudwatchDimensionId']])
                    else:
                        # [ "AWS/States", "ExecutionsFailed", "StateMachineArn", "arn:aws:states:us-west-2:ACCOUNTID:stateMachine:CloudVelumBuilderStateMachine-Xm2QclLByXty" ]
                        block.append(
                            [
                                service.cloudwatch_namespace,
                                metric,
                                service.cloudwatch_dimension,
                                resource['cloudwatchDimensionId']
                            ]
                        )

                    after_first = True

                metric_properties = {
                    'metrics': block,
                    'view': 'timeSeries',
                    'stacked': False,
                    'region': REGION,
                    'title': metric,
                    'legend': {
                            'position': 'bottom'
                    },
                    'yAxis': {
                        'left': {
                            'label': ''
                        },
                        'right': {
                            'label': ''
                        }
                    }
                }

                # Add any dashboard overrides for the specific metric
                metric_additions = service.dashboard_additions.get(metric, {})
                widget_metric_properties = {
                    **metric_properties,
                    **metric_additions
                }

                widget_metric = {
                    'type': 'metric',
                    'width': 12,
                    'height': 6,
                    'properties': widget_metric_properties
                }

                dashboard_widgets.append(widget_metric)

        return dashboard_widgets
