import boto3
import json

SM_ARN = 'arn:aws:states:us-east-1:960351580303:stateMachine:MyStateMachine-FQtos34IL17v'

sm = boto3.client('stepfunctions')
def lambda_api(event, context):
    try:
        # Load data coming from APIGateway
        data = json.loads(event['body'])
        data['waitSeconds'] = int(data['waitSeconds'])
        
        # Start the state machine execution
        sm.start_execution(stateMachineArn=SM_ARN, input=json.dumps(data))
        
        response = {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"Status": "Success"})
        }
    except Exception as e:
        # If an error occurs during processing, return an error response
        response = {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"Status": "Error", "Message": str(e)})
        }
    
    return response
