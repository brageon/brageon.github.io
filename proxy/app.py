import sys, boto3, json, jinja2
from flask import Flask, request, jsonify, render_template
sys.path.insert(1, '../')
from login.mov import botox

app = Flask(__name__, static_folder='static', template_folder='templates')
bot = botox(True)
bot.setup()

lambda_client = boto3.client('lambda')
@app.route('/', methods=['GET', 'POST'])
def send_payload():
    if request.method == 'GET':
        title = "Pipeline with CORS"
        return render_template('index.html', title=title)
    if request.method == 'POST':
        message = request.data.decode('utf-8')
        payload = {'body': message}
        lambda_response = lambda_client.invoke(FunctionName='Darwin', Payload=json.dumps(payload).encode('utf-8'), InvocationType='RequestResponse')
        parsed_response = lambda_response['Payload'].read().decode('utf-8') 
        return jsonify(parsed_response)

if __name__ == '__main__':
    app.run(debug=True)
