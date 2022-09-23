
from aws_cdk import (
    # Duration,
    Stack,
    # core as cdk,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_logs as logs,
    aws_elasticloadbalancingv2 as elbv2,
    App,
    # aws_sqs as sqs,
)
from constructs import Construct
#  from constructs import Construct
#  from aws_cdk import App, Stack
import aws_cdk as cdk
# import logging as logs

# from cdk import 

class S6makECSStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, repo = ecr.Repository,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.repo = repo 
        cdk.CfnOutput(self, "makrepoName1", value=repo.repository_name)
        # cdk.CfnOutput(self, "MubarizrepoName2", value=repo.repository_name)
        self.create_ecs_cluster()
        self.create_task_definition()
        self.create_fargate_service()
    
    ## Create ecs
    def create_ecs_cluster(self):
        '''
            URL:
            [*]--------> self.ecs_cluster -> A regional grouping of one or more container instances on which you can run tasks and services.
                                    params:
                                        cluster_name (Optional[str]) – The name for the cluster. Default: CloudFormation-generated name
                                        
                                        container_insights (Optional[bool]) – If true CloudWatch Container Insights will be enabled for the cluster.
                                                                              Default: - Container Insights will be disabled for this cluser.
                                                                              
                                        enable_fargate_capacity_providers (Optional[bool]) – Whether to enable Fargate Capacity Providers. 
                                                                                            Default: false
                                        vpc (Optional[IVpc]) – The VPC where your ECS instances will be running or your ENIs will be deployed. 
                                        Default: - creates a new VPC with two AZs
            
            
            
            [*]--------> VPC -> Define an AWS Virtual Private Cloud.
                                See the package-level documentation of this package for an overview of the various dimensions 
                                in which you can configure your VPC.
                                
                            params: 
                                   max_azs:  Define the maximum number of AZs to use in this region. 
                                             If the region has more AZs than you want to use (for example, because of EIP limits), 
                                             pick a lower number here. The AZs will be sorted and picked from the start of the list. 
                                             If you pick a higher number than the number of AZs in the region, all AZs in the region will be selected. 
                                             To use “all AZs” available to your account, use a high number (such as 99). 
                                             Default: 3
            
        
        
        '''
        self.vpc = ec2.Vpc(self, "mak_ecs_vpc2", max_azs=3)
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecs/Cluster.html
        self.ecs_cluster = ecs.Cluster(self, 'mak-ecs_cluster2', 
            cluster_name = "mak_FargetCluster2",
            # If true CloudWatch Container Insights will be enabled for the cluster. Default: - Container Insights will be disabled
            container_insights=True,
            # Whether to enable Fargate Capacity Providers. Default: false
            enable_fargate_capacity_providers = True,
            vpc = self.vpc,
        )
        
    # Create Task defination
    def create_task_definition(self):
        
        '''
        
           [*]---------self.ecstask_role ---> will assign policies needed for the task services
           
           [*]---------self.fargate_task_definition ---> The details of a task definition run on a Fargate cluster.
                                        params: 
                                                cpu--> The number of cpu units used by the task.
                                                
                                                memory_limit_mib--> The amount (in MiB) of memory used by the task.
                                                
                                                ephemeral_storage_gib---> he amount (in GiB) of ephemeral storage to be allocated to the task. 
                                                                          The maximum supported value is 200 GiB
                                                task_role = self.ecstask_role
                                                
            [*]--------self.fargate_task_definition.add_container---> Adds a new container to the task definition.
                                        params: 
                                                
                                               cpu--> The number of cpu units used by the task.
                                               memory_limit --> The amount (in MiB) of memory used by the task.
                                               environment -> The environment variables to pass to the container.
                                               
                                               image --> The image used to start a container. This string is passed directly to the Docker daemon.
                                                            Images in the Docker Hub registry are available by default.
                                                            
                                               logging -> The log configuration specification for the container. 
                                               
                                               port_mapping: The port mappings to add to the container definition, 
                                                             Port mappings allow containers to access ports on the host container 
                                                             instance to send or receive traffic.
                                                
        
        '''
        
        self.ecstask_role = self.create_ecs_task_role()
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_logs/LogGroup.html
        # Define a CloudWatch Log Group.
        ecs_task_log = logs.LogGroup(self, "mak-ecs-task-log-group12", 
        # Name of the log group. Default: Automatically generated
            #log_group_name = "ecs-task-log-group1",
            # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_logs/RetentionDays.html#aws_cdk.aws_logs.RetentionDays
            # How long the logs contents will be retained
            retention = logs.RetentionDays.FIVE_DAYS
        )
        
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecs/FargateTaskDefination.html
        self.fargate_task_definition = ecs.FargateTaskDefinition(self, "mak_FargetTaskDef12",
            # the number of cpu units used by the task
            cpu=256,
            memory_limit_mib=512,
            ephemeral_storage_gib = 21,
            task_role=self.ecstask_role,
            # family (Optional[str]) - The name oa a family that this task defination is registered to. A family group multiple version
            # Default: - Automatically generated name
            family="mak_ecs_task_family12",
            
        )
        
        task_environment = {
            "ENV1": "environment variable",
        }
        
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecs/FargateTaskDefination.html@aws_cdk.aws_ecs.FargateTaskDefinition
        self.fargate_task_definition.add_container("MaktaskContainer2", 
            # The name of the conatiner. Default: - id of node associated with ContainerDefinition.
            container_name="MaktaskContainer12",
            cpu=256,
            memory_limit_mib=512,
            # The environment variable to pass to the conatiner. Default: - No environment variable.
            environment = task_environment,
            # True: if the container fails or stops for any reason, all other containers that are part of the task are stopped.
            # False: then its failure does not afect the rest of the containers in a task. All tasks must have at least one essential
            # Default is True
            essential=True,
            # the image used to start a container. The sting is passed directly to the Docker daemon.
            # Images in the Docker Hub registry are availableby default. 
            image=ecs.ContainerImage.from_ecr_repository(repository=self.repo),
            logging=ecs.LogDriver.aws_logs(stream_prefix='mak-ecs-task12', log_group=ecs_task_log),
            port_mappings=[ecs.PortMapping(
                # The port number on the container that is bound to the user-specfied
                container_port=8801,
                protocol=ecs.Protocol.TCP
                )
                
            ],
            )
        
    def create_ecs_task_role(self):
        sts_policy = iam.PolicyStatement(actions=['sts:AssumRole'], resources = ["*"])
        cw_policy = iam.PolicyStatement(actions=['logs:*'], resources = ["*"])
        task_role_policy_document = iam.PolicyDocument(statements= [sts_policy, cw_policy])
        
        return iam.Role(self, "mak-ecs-task-role12",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            description = "ECS task role for package forecast app",
            managed_policies = [iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")],
            inline_policies = [task_role_policy_document]
        )        
    
    def create_fargate_service(self):
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecs?FargateService.html
        
        '''
            This creates a service using the Fargate lauch type on an ECS cluster.
            [*]--------------- ecs.FargateService ----> 
                                                params:
                                                task_definition: already defined above
                                                
                                                cluster: already defined above
                                                
                                                desired_count: The desired number of instantiations of the task definition to keep running on the service. 
                                                balancer is in-use and it is not already set

                                                max_healthy_percent: The maximum number of tasks, specified as a percentage of the
                                                                     Amazon ECS service’s DesiredCount value,
                                                                     that can run in a service during a deployment
                                                
                                                min_healthy_percent: The minimum number of tasks, 
                                                                     specified as a percentage of the Amazon ECS service’s DesiredCount value,
                                                                     that must continue to run and remain healthy during a deployment
                                                                     
                                                                     
                                                                     
                                                        
        '''
        
        service = ecs.FargateService(self, "makEcsService2",
            service_name="MakEcsService2",
            cluster=self.ecs_cluster,
            task_definition=self.fargate_task_definition,
            desired_count=100,
            min_healthy_percent=10,
            max_healthy_percent=100,
        )
        
        # Define an App Load Balancer
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_elasticloadbalancingv2/ApplicationLoadBalancer.html
        lb = elbv2.ApplicationLoadBalancer(self, "LB2", 
            vpc=self.vpc,
            internet_facing=True
        )
        
        listener = lb.add_listener("MakListener2", port=80)
        
        service.register_load_balancer_targets(
            ecs.EcsTarget(
                container_name="MaktaskContainer12",
                container_port=8801,
                new_target_group_id="ECS2",
                listener=ecs.ListenerConfig.application_listener(listener, 
                    protocol=elbv2.ApplicationProtocol.HTTP
                ))
            )
            
        cdk.CfnOutput(self, "MakLoadBalancerDNS2", value=lb.load_balancer_dns_name)