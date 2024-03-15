import boto3
import pandas as pd
from io import BytesIO
from io import StringIO

bucket, filename = "aswlambdaassignment1bucketaccesslogs", "store_data.csv"


s3_client = boto3.client("s3")
response = s3_client.get_object(Bucket=bucket, Key=filename)
file_content = response["Body"].read().decode('utf-8')

# Read the content using pandas
data = pd.read_csv(StringIO(file_content))
print(data)
print(data['store_id'] == 104)
