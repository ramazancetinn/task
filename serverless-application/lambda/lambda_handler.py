import json
import csv
import boto3


def main(event, context):
    
    # set region to eu-west-1
    region = "eu-west-1"
    record_list = []
    
    try:
        s3 = boto3.client("s3")
        
        dynamodb = boto3.client('dynamodb', region_name = region)
        # example 's3 PUT event' sample
        """
            {
            "Records": [
                {
                "eventVersion": "2.0",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "1970-01-01T00:00:00.000Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "EXAMPLE"
                },
                "requestParameters": {
                    "sourceIPAddress": "127.0.0.1"
                },
                "responseElements": {
                    "x-amz-request-id": "EXAMPLE123456789",
                    "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "testConfigRule",
                    "bucket": {
                    "name": "example-bucket",
                    "ownerIdentity": {
                        "principalId": "EXAMPLE"
                    },
                    "arn": "arn:aws:s3:::example-bucket"
                    },
                    "object": {
                    "key": "test%2Fkey",
                    "size": 1024,
                    "eTag": "0123456789abcdef0123456789abcdef",
                    "sequencer": "0A1B2C3D4E5F678901"
                    }
                }
                }
            ]
            }
        """

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        csv_file = s3.get_object(Bucket = bucket, Key = key)
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(record_list, delimiter=',', quotechar='"')
        
        for row in csv_reader:
            id = row[0]
            film = row[1]
            genre = row[2]
            lead_studio = row[3]
            year = row[4]
            
            # put item to table
            dynamodb.put_item(
                TableName = 'Movies',
                Item = {
                    'id': {'N': id}, 
                    'film': {'S': film},
                    'genre': {'S': genre},
                    'lead_studio': {'S': lead_studio},
                    'year': {'N': year},
                })
        
    except Exception as e:
        raise e
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV successfully imported to DynamoDB Table.')
    }
