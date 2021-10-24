#!/usr/bin/env python3
import os
from aws_cdk import core

from eks_iaac.eks_iaac import EKSIaac
from ecr_iaac.ecr_iaac import ECRIaac


app = core.App()

EKSIaac(app, "EKSStack",env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region="eu-west-1"))
ECRIaac(app, "ECRStack",env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region="eu-west-1"))

app.synth()
