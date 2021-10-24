from aws_cdk import aws_s3, core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_notifications
from aws_cdk import aws_lambda

# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_dynamodb as dynamodb


class CsvImporter(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # create dynamodb table named 'Movies'
        dynamodb.Table(self, "Create DynamoDB Table",
            table_name="Movies",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.NUMBER)
        )


        # create bucket named 'serverless-application-bucket-2021-10-27'
        bucket = s3.Bucket(self, "Create Bucket", bucket_name="serverless-application-bucket-2021-10-27")

        # create lambda function
        function = aws_lambda.Function(self, "Lambda Function",
                                        runtime=aws_lambda.Runtime.PYTHON_3_9,
                                        handler="lambda_handler.main",
                                        code=aws_lambda.Code.asset("./lambda"))

        # create an event notification for 's3 PUT'  only .csv files
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, 
                                        aws_s3_notifications.LambdaDestination(function),
                                        s3.NotificationKeyFilter(suffix=".csv"))





