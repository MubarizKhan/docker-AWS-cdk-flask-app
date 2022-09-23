from aws_cdk import (
    Stack,
    aws_ecr as ecr, #Define a repository by creating a new instance of Repository. A repository holds multiple verions of a single container image.
    aws_ecr_assets as ecra,
)
from constructs import Construct

import cdk_ecr_deployment as ecrdeploy 

class makECRStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.ecr_repository=self.create_ecr_repositry()
        self.create_and_deploy_image()
        
    # Create ECR
    def create_ecr_repositry(self):
        
        '''
            URL: https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr/Repository.html
            ------------------ returns elastic container registry's repository -----------------------------
            
            
            [*]--------  image_scan_on_push -> Image scanning helps in identifying software vulnerabilities in your container images.
                                               Ensures that each new image pushed to the repository is scanned
            
            [*]--------  image_tag_mutability -> You can set tag immutability on images in our repository using the imageTagMutability construct prop.
            
                        image_tag_mutability = ecr.TagMutability.IMMUTABLE ->  The tag mutability setting for the repository. default MUTABLE
                                                                                all image tags within the repository will be immutable which will
                                                                                prevent them from being overwritten.
                                                                                
            URL: https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr/LifecycleRule.html
            [*]--------  lifecycle_rules -> Lifecycle policies help which managing the lifecycle of the images in your repositories.
                                            You define rules that result in the cleaning up of unused images.
        '''
        return ecr.Repository(self, "mak_ecr_repo",
            # Name for this repository. Default: Automatically generated name.
            repository_name = "mak_ecr_repo",
            image_scan_on_push=True,
 
            image_tag_mutability= ecr.TagMutability.IMMUTABLE,

            lifecycle_rules = [
               
                ecr.LifecycleRule(
                    description="Only retain 200 images",
                    max_image_count=200,      # The maximum number of images to retain
                    rule_priority=1,
                    
                    )
                ]
            )
            
    # Create Image
    def create_and_deploy_image(self):
        
        '''
            URL: https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr_assets/DockerImageAsset.html
            ------------------------------- aws_ecr_assets ----------------------------------------------------------
            An asset that represents a Docker image.The image will be created in build time and uploaded to an ECR repository.   
            [*]------------- Image = ecra.DockerImageAsset --------------
                -----Params
                                directory (str) – The directory where the Dockerfile is stored. 
                                                  Any directory inside with a name that matches the CDK output folder (cdk.out by default)
                                                  will be excluded from the asset.
        
        
            URL: https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr_assests/README.html#publishing-images-to-ecr-repositories
            ------------ ------------------ecrdeploy.ECRDeployment ----------------------------------
            [*]--------------If you are looking for a way to publish image assets to an ECR repository in your control,
                            you should consider using cdklabs/cdk-ecr-deployment, 
                            which is able to replicate an image asset from the CDK-controlled ECR repository to a repository of your choice.    
        
        '''
        
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr_assets/README.html
        image = ecra.DockerImageAsset(self, "mak-flask-image",
            # The directory where the Dockerfile is stored.
            directory = './app'
            
        )
        
        # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_ecr_assests/README.html#publishing-images-to-ecr-repositories
        ecrdeploy.ECRDeployment(self, 'makf1',
            src = ecrdeploy.DockerImageName(image.image_uri),
            dest=ecrdeploy.DockerImageName(f"{self.ecr_repository.repository_uri}:latest"),
            
        );