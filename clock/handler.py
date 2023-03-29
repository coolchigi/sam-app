import datetime
from datetime import datetime
import dateutil.tz

import json


def clock(event, context):
    
    query_params = event.get('queryStringParameters')

    # Extract the 'time' parameter
    time_zone = query_params.get('time')

    if(time_zone is None):
            message = f"The time in GMT 0 is {time_zone}"
    elif(time_zone is not None):
        eastern = dateutil.tz.gettz('US/Eastern')
        time_in_timezone  = datetime.now(tz=eastern)
        message = f"The time in {time_zone}, is {time_in_timezone}"

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                'message' : message
            }, default=str
        ),
    }


#import boto3

# dynamodb = boto3.resource('dynamodb')
# table_name = 'my-visitors-table'
# counter_key = 'visitors_count'

# def lambda_handler(event, context):
#     # Get the DynamoDB table
#     table = dynamodb.Table(table_name)
    
#     # Get the current visitor count
#     response = table.get_item(
#         Key={
#             'counter_name': counter_key
#         }
#     )
#     count = response.get('Item', {}).get('count', 0)
    
#     # Increment the visitor count
#     count += 1
    
#     # Update the DynamoDB table with the new count
#     table.put_item(
#         Item={
#             'counter_name': counter_key,
#             'count': count
#         }
#     )
    
#     # Return the current visitor count
#     return {
#         'statusCode': 200,
#         'body': f'Welcome! You are visitor number {count}.'
#     }


# Resources:
#   DynamoDBTable:
#     Type: "AWS::DynamoDB::Table"
#     Properties:
#       AttributeDefinitions:
#         - AttributeName: "pk"
#           AttributeType: "S"
#         - AttributeName: "sk"
#           AttributeType: "S"
#       KeySchema:
#         - AttributeName: "pk"
#           KeyType: "HASH"
#         - AttributeName: "sk"
#           KeyType: "RANGE"
#       BillingMode: PAY_PER_REQUEST

#   LambdaFunction:
#     Type: "AWS::Serverless::Function"
#     Properties:
#       Handler: lambda_function.lambda_handler
#       Runtime: python3.8
#       CodeUri: .
#       MemorySize: 128
#       Timeout: 10
#       Policies:
#         - AmazonDynamoDBFullAccess
#       Events:
#         GetVisits:
#           Type: HttpApi
#           Properties:
#             Path: /visits
#             Method: get
#         IncrementVisits:
#           Type: HttpApi
#           Properties:
#             Path: /visits
#             Method: post

# import json
# import boto3

# dynamodb = boto3.client('dynamodb')

# def lambda_handler(event, context):
#     # Get current count
#     current_count = get_count()

#     # Increment count
#     increment_count()

#     # Construct response
#     response = {
#         'visits': current_count + 1
#     }

#     return {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': json.dumps(response)
#     }

# def get_count():
#     response = dynamodb.get_item(
#         TableName='DynamoDBTable',
#         Key={
#             'pk': {'S': 'count'},
#             'sk': {'S': 'counter_key'}
#         }
#     )

#     if


# import boto3
# import os

# dynamodb = boto3.client('dynamodb')
# counter_table = os.environ['COUNTER_TABLE']

# def lambda_handler(event, context):
#     # Retrieve the visitor count from DynamoDB
#     response = dynamodb.get_item(
#         TableName=counter_table,
#         Key={
#             'pk': {'S': 'count'},
#             'sk': {'S': 'total_visitors'}
#         }
#     )

#     # Parse the response and retrieve the visitor count
#     item = response.get('Item')
#     visitor_count = item.get('visitor_count').get('N')

#     # Return the visitor count as a response
#     return {
#         'statusCode': 200,
#         'body': {
#             'visitor_count': visitor_count
#         }
#     }


# Resources:
#   CounterTable:
#     Type: AWS::DynamoDB::Table
#     Properties:
#       AttributeDefinitions:
#         - AttributeName: pk
#           AttributeType: S
#         - AttributeName: sk
#           AttributeType: S
#       KeySchema:
#         - AttributeName: pk
#           KeyType: HASH
#         - AttributeName: sk
#           KeyType: RANGE
#       ProvisionedThroughput:
#         ReadCapacityUnits: 1
#         WriteCapacityUnits: 1

#   VisitorCounter:
#     Type: AWS::Serverless::Function
#     Properties:
#       CodeUri: visitor-counter/
#       Handler: app.lambda_handler
#       Runtime: python3.8
#       Policies:
#         - AmazonDynamoDBFullAccess
#       Environment:
#         COUNTER_TABLE: !Ref CounterTable
#       Events:
#         GetRequest:
#           Type: Api
#           Properties:
#             Path: /visitors
#             Method: get
