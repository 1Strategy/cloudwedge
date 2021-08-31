---
title: CloudVelum
---

<p align="center">
    <div class="banner-image"></div>
</p>

<p align="center">
    <em>CloudVelum is an AWS Cloudwatch monitoring framework that accelerates your ability to get up and running with native AWS monitoring services.</em>
</p>

---

!!! failure "CloudVelum is not"

    - A competitor to more robust, but more expensive 💲💲💲, Application Performance Monitoring tools like DataDog, New Relic, Dynatrace, App Dynamcis etc..
    - A fully customizable enterprise suite of monitoring tools with beautiful dashboard visualizations and stand-alone app support for all of your devices.
    - An infinitely scalable monitoring tool.

!!! success "CloudVelum is"

    - A tool to automate away the complexity of setting up CloudWatch Alarms and Dashboards and facilitate alert notifications when those CloudWatch Alarms are breached.
    - An inexpensive, easy to deploy, set of native AWS tools/services to get you up and running with monitoring and alerting on AWS.
    - Easy to use — Just add tags!
    - Better than nothing.
    - Extensible.
    - Multi-account/Multi-region. *(Coming soon)*

??? question "What does CloudVelum mean?"

    Velum is latin for 'veil' or covering.

    The Google definition:
    >  "a membrane or membranous structure, typically covering another structure or partly obscuring an opening"

    And a little more information:
    >
    Velum clouds are actually accessory clouds which depend on the parent cloud for their formation and continuance. Velum appears as a thin patch of horizontal cloud located either above or on the sides of the parent cloud. It is like a pileus cloud that looks like a cap on top of cumulus clouds but it is less appealing and rather boring. [^1]

    So, why the name?

    Well, CloudVelum is sort of a covering over your existing AWS Cloud resources. Its functions and behavior is transparent, you can look and see everything its doing, so the idea of a veil fits well. You can see through a veil. But it does help cover some of the complexity behind the scenes. CloudVelum is going to 'veil' the implementation details of setting up CloudWatch Alarms and Dashboards. But whenever you want, part the veil and see whats there.

## Why use CloudVelum

CloudVelum is perfect for when you want to use the native AWS monitoring services, but you dont want to fuss with the all the implementation details. CloudVelum will provide the monitoring alarms and the dashboards you would have built by hand (or in CloudFormation) and give you back that time to focus on what really matters. Essentially, CloudVelum is doing the "undifferentiated heavy lifting" of setting up CloudWatch and and wiring it into an alerting pipeline.

The key features are:

- **Native AWS**: CloudVelum is using 100% AWS native services from the cradle to the grave.
- **100% Privacy**: Your data never leaves your account. No 3rd party to ship data to, its all contained within the walls of your own home. Look at the source code yourself, we are not hiding anything. You have total control.
- **Operationally Easy**: You only have to learn the custom CloudVelum "tags" and add them to your resources.
- **Opt-In Only**: You choose what to monitoring and how.
- **Event Based**: You change your environment, CloudVelum will update itself. Its not as sophisticated as true AI, but you might start to think so.

## How CloudVelum works

<p align="center">
    <div class="banner-graphic"></div>
</p>

Getting a little more technical, here is a breakdown of the interactions between you, AWS and CloudVelum:

| Actor | Activity                                                                                                                                                          |
| :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  👩🏾‍💻   | You tag a resource with a CloudVelum supported tag                                                                                                                |
|  ☁️   | AWS captures user activity in AWS EventBridge                                                                                                                      |
|  🤖   | CloudVelum watches AWS EventBridge for any relevant events. In this case, it sees a CloudVelum tag was added so it decides it needs to work.                     |
|  🤖   | CloudVelum starts an AWS StepFunction which orchestrates the CloudVelum activity                                                                                  |
|  🤖   | CloudVelum uses the AWS apis to get all the resources in your account that have opted-in to be monitoring be CloudVelum.                                          |
|  🤖   | CloudVelum iterates over those resources and builds a CloudFormation template which has all the AWS CloudWatch alarms and dashboards created for those resources. |
|  🤖   | CloudVelum uses the AWS CloudFormation api to deploy the CloudFormation template, which does all the creation of the alarms and dashboards.                       |
|  ☁️   | AWS sends you a bill                                                                                                                                              |
|  👩🏾‍💻   | You do more important things                                                                                                                                      |

## Example Usage

You can get started monitoring with CloudVelum by using the following CloudVelum core tags. Just slap this a tag called `cloudvelum:active` on a supported service and watch the alarms get created. Review all the supported tags.

???+ velum-tag "cloudvelum:active"

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

## Deployment

CloudVelum is packaged in a CloudFormation template. This makes is very easy to deploy. You just need to get a url reference to the pre-baked CloudFormation and then use the AWS CloudFormation console to deploy the stack into your account. The Deploy button below will open your AWS Console in the `us-west-2` region and load the CloudVelum CloudFormation reference for you to review and deploy.

[Deploy CloudVelum :octicons-rocket-16:](./tutorial/#to-deploy){: .md-button .md-button--primary .center-it }

## Getting Started

It's always nice to have someone show you around a new place. Check out the [Getting Started](./tutorial/index.md) guide to get comfortable using CloudVelum.

[Get Started :octicons-mortar-board-16:](./tutorial/index.md){: .md-button .md-button--small .md-button--secondary .center-it }

## License

This project is licensed under the terms of the MIT license.

[^1]: Learn about Velum Clouds here: https://whatsthiscloud.com/cloud-accessories/velum/
