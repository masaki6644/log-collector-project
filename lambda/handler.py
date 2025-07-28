import json
import boto3
import uuid
import datetime

s3 = boto3.client('s3')
BUCKET_NAME = "mylog-storage-bucket"  # 必ず自分のS3バケット名にする

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])  # API Gateway経由で来るbodyをパース
        filename = f"{datetime.datetime.utcnow().isoformat()}_{uuid.uuid4()}.json"
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=json.dumps(data))
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Saved', 'file': filename})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

