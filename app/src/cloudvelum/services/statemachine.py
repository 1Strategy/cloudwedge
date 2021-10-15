"""
StateMachine for CloudVelum

Provides implementation details for statemachine service. It follows contract
outlined in cloudvelum.models.AWSService
"""

from os import environ
from typing import Any, Dict, List, Optional

import boto3
import jmespath

from cloudvelum.models import AWSResource, AWSService
from cloudvelum.utils.logger import get_logger
from cloudvelum.utils.tags import TagsApi

REGION = environ.get('REGION')

LOGGER = get_logger("cloudvelum.statemachine")


# Model for Service, extending AWSResource
class StateMachineResource(AWSResource):
    pass

# Class for Service
class StateMachineService(AWSService):
    # Name of the service, must be unique
    name = "statemachine"
    # Cloudwatch alarm service specific values
    cloudwatch_namespace = "AWS/States"
    cloudwatch_dashboard_section_title = "States"
    cloudwatch_dimension = "StateMachineArn"

    # Default metric to be used when metrics are not explicit in tags
    default_metrics = ["ExecutionsFailed",
                        "ExecutionThrottled",
                        "ExecutionTime"]
    # Alarm defaults for the service, applied if metric default doesnt exist
    default_alarm_props = {
        'Statistic': "Sum"
    }

    # List of supported metrics and default configurations
    supported_metrics = {
        'ExecutionsStarted': {},
        'ExecutionThrottled': {},
        'ExecutionsAborted': {},
        'ExecutionsSucceeded': {},
        'ExecutionsFailed': {},
        'ExecutionsTimedOut': {},
        'ExecutionTime': {}
    }

    # There are dashboard additions that can be added at the metric level
    override_dashboard_metric_properties = {}

    @staticmethod
    def build_dashboard_widgets(resources: List[StateMachineResource]) -> List[Any]:
        """
        Build dashboard widgets for the resources
        """

        # Get widgets with base method (like calling super)
        return AWSService.build_dashboard_widgets(StateMachineService, resources)

    @ staticmethod
    def get_resources(session: boto3.session.Session) -> List[StateMachineResource]:
        """
        Return all AWS StateMachine resources within scope, based on the tags
        """

        try:

            # Get things in a neat statemachine resource object
            cleaned_resources: List[StateMachineResource] = []

            # Get paginator for service
            paginator = session.client('stepfunctions').get_paginator(
                'list_state_machines').paginate()

            # Collect all resources
            for page_resources in paginator:
                for state_machine in page_resources['stateMachines']:

                    state_arn = state_machine['stateMachineArn']

                    # For each state, get the tags
                    states_resource_tags = session.client('stepfunctions').list_tags_for_resource(
                        resourceArn=state_arn)

                    states_tags = states_resource_tags['tags']

                    # Keys for the tags are 'key' and 'value' so convert that to capitalize
                    converted_tags = TagsApi.convert_lowercase_tags_keys(
                        states_tags)

                    # If the active monitoring tag is on the instance, include in resource collection
                    # Stripping key so no whitespace mismatch
                    if any((tag['Key'].strip() == AWSService.TAG_ACTIVE and tag['Value'] == 'true') for tag in converted_tags):
                        # This resource has opted in to cloudvelum

                        # Get values from tags if they exist
                        owner_from_tag = TagsApi.get_owner_from_tags(converted_tags)
                        name_from_tag = TagsApi.get_name_from_tags(converted_tags)
                        state_name = state_machine['name']

                        # Setup StateMachine values
                        service = StateMachineService.name
                        resource_name = name_from_tag or state_name
                        resource_id = state_arn
                        resource_owner = owner_from_tag
                        tags = converted_tags

                        # Create StateMachine
                        clean_resource = StateMachineResource(
                            service=service,
                            name=resource_name,
                            uniqueId=resource_name,
                            cloudwatchDimensionId=resource_id,
                            owner=resource_owner,
                            tags=tags
                        )

                        # Add to collection
                        cleaned_resources.append(clean_resource)

            return cleaned_resources

        except Exception as err:
            LOGGER.info(
                f"Failed to get resources information with error: {err}")
            raise err
