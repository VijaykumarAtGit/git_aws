import boto3
import pandas as pd
from io import BytesIO
from io import StringIO
import json

bucket= "aswlambdaassignment1bucketaccesslogs"
filename = "2024-03-09_raw_input.json"
sns_arn = 'arn:aws:sns:us-east-1:120582745863:doordashNotification'


s3_client = boto3.client("s3")
sns_client = boto3.client('sns')

# Read the content using pandas
response = s3_client.get_object(Bucket=bucket, Key=filename)
file_content = response["Body"].read().decode('utf-8')
data = json.loads(file_content)
print((data))

# processing data in the dataframe
i = 0
new_json_list = []
for i in range(len(data)):
    print( data[i]['1'] , data[i]['delivered'] )
    if data[i]['delivered'] == 'delivered' :
        new_json_list.append(data[i])

# write json file back to s3
json_str = json.dumps(new_json_list)
s3_client.put_object(
    Bucket=bucket,
    Key="new_" + filename,
    Body=json_str,
)


# send sns message to the subscriber
respone = sns_client.publish(Subject="SUCCESS - Daily Data Processing", TargetArn=sns_arn, Message="Message",
                             MessageStructure='text')
print("Response is ------------> ", respone)






