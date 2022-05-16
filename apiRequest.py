# Script calls API Endpoint and prints the response in JSON.  When adding this as a Lambda in AWS, make sure you have a Layer added 
# that contains the Requests libary as this is not supoported natively by AWS Lambda.  Zip file for Lambda layer is in the repo.

import requests

def lambda_handler(event, context):
   response = requests.post("***ADD API HTTP END POINT HERE***",)
   print(response.json())
