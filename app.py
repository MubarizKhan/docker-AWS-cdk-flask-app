#!/usr/bin/env python3
import os

import aws_cdk as cdk
#  from constructs import Construct
from aws_cdk import App, Stack
from sprint6_mubariz.sprint6_mubariz_stack import makECRStack
from sprint6_mubariz.sprint6_mubariz_ecs import S6makECSStack
#!/usr/bin/env python3

app = cdk.App()

cdk.Tags.of(app).add("cohort", "Voyager")
cdk.Tags.of(app).add("name", "Mubariz")


ecr_stack = makECRStack(app, "Sprint6MAKECRStack3", env=cdk.Environment(account='315997497220', region='us-east-1'))
ecs_stack = S6makECSStack(app, "Sprint6MAKECSStack3", repo=ecr_stack.ecr_repository, env=cdk.Environment(account='315997497220', region='us-east-1')
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
ecs_stack.add_dependency(ecr_stack, "All contanier dependency should be there")

app.synth()