import sys, boto3, botocore
from flask_cors import CORS
from flask import Flask, request
sys.path.insert(1, '../')
from login.mov import botox
app = Flask(__name__)
bot = botox(True)
bot.setup()
CORS(app)

lambda_client = boto3.client('lambda') 
@app.route('/', methods=['GET', 'POST'])
def trigger_workflow():
    message = request.form
    lambda_response = lambda_client.invoke(
    FunctionName='Darwin', Payload=message,
    InvocationType='RequestResponse')   
    parsed_response = lambda_response['Payload'].read().decode('utf-8')
    return parsed_response

if __name__ == '__main__':
    app.run() 