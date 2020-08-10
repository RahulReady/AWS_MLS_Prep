
# Make sure you have the correct permissions setup.
# The lambda function should have read access to S3 buckets.
# ** Note- If you are getting a timeout message, increase the 'timeout' time under 'Basic Settings'

import boto3
def lambda_handler(event, context):

    rekognition = boto3.client('rekognition')

    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': 'INSERT BUCKET NAME HERE',
                'Name': 'INSERT FILE NAME HERE'
            }
        }
    )

    text = ''

    for detection in response['TextDetections']:
        if detection['Type'] == "WORD":
            text = text + ' ' + detection['DetectedText']

    return {
        'statusCode': 200,
        'body': text.strip()
        }
