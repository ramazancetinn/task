from aws_cdk import  aws_ecr as ecr
from aws_cdk import  core

class ECRIaac(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr.Repository(self, "Repository", repository_name="web-app")