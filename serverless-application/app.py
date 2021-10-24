#!/usr/bin/env python3
import os

from aws_cdk import core

from csv_importer.csv_importer import CsvImporter



app = core.App()

CsvImporter(app, "ServerlessApplicationStack",
    env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region="eu-west-1")
)

app.synth()


