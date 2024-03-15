import boto3
import json

def lambdaProcessing():
    """ This function will check presence of lambda function"""
    lambdaClient = boto3.client("lambda")
    response = ''
    i = 0
    try:
        response = lambdaClient.list_functions()
        print("number of functions {}".format( len( response['Functions'])))

        jsonLoad = [x['FunctionName'] for x in response['Functions']]

    except Exception as e :
        print(e)
    finally:
        print(response)



if __name__ == "__main__":
    lambdaProcessing()