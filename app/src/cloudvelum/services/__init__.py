"""
Services

Register supported services classes for consumption
"""

from typing import List

from cloudvelum.models import AWSService

from .ec2 import EC2Service
from .autoscalinggroup import AutoScalingGroupService
from .rds import RDSService
from .elasticbeanstalk import ElasticBeanstalkService
from .apigateway import ApiGatewayService
from .statemachine import StateMachineService
from .ecs import ECSService


class ServiceRegistry():
    # This list will be used to iterate through each supported service
    supported: List[AWSService] = [
        EC2Service,
        RDSService,
        ElasticBeanstalkService,
        ApiGatewayService,
        StateMachineService,
        ECSService,
        AutoScalingGroupService
    ]

    @staticmethod
    def get_service(service_name: str) -> AWSService:

        # Add service to the lookup based on its 'service.name'
        # TODO: maybe we can loop through supported services and find the match
        # basically just want to provide a quick way to lookup service dynamically
        registry = {
            'ec2': EC2Service,
            'autoscalinggroup': AutoScalingGroupService,
            'rds': RDSService,
            'elasticbeanstalk': ElasticBeanstalkService,
            'apigateway': ApiGatewayService,
            'statemachine': StateMachineService,
            'ecs': ECSService
        }

        return registry[service_name]
