import boto3



def lambda_handler(event, context):
    # read the S3 bucket name and the file loaded to S3
    print(event['Records'][0]['s3']['object']['key'])
    print(event['Records'][0]['s3']['bucket']['name'])
    bucketName = event['Records'][0]['s3']['bucket']['name']
    objectName = event['Records'][0]['s3']['object']['key']

    s3_client = boto3.client("s3")
    response  = s3_client.get_object(Bucket=bucketName, Key = objectName)
    print(response)