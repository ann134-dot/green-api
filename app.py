from flask import Flask, render_template, jsonify
import requests
from flask import request as flaskRequest
 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getSettings')
def get_settings():
    instanceId = flaskRequest.args.get('instanceId')
    api_token = flaskRequest.args.get('apiInstanceToken')

    api_url = f"https://api.green-api.com/waInstance{instanceId}/getSettings/{api_token}"
    response = requests.get(api_url)
    
    if not response.ok:
        data = {'code': response.status_code, 'content': response.text}
        return jsonify(data)
    
    data = response.json()
    return jsonify(data)

@app.route('/getStateInstance')
def get_state_instance():
    instanceId = flaskRequest.args.get('instanceId')
    api_token = flaskRequest.args.get('apiInstanceToken')

    api_url = f"https://api.green-api.com/waInstance{instanceId}/getStateInstance/{api_token}"
    response = requests.get(api_url)
    
    if not response.ok:
        data = {'code': response.status_code, 'content': response.text}
        return jsonify(data)
    
    data = response.json()
    return jsonify(data)


@app.route('/sendMessage', methods=['POST'])
def send_message():
    instanceId = flaskRequest.args.get('instanceId')
    api_token = flaskRequest.args.get('apiInstanceToken')
    data = flaskRequest.get_json()
    msg = data.get('message')
    chat_id = data.get('chatId')
    chat_id = chat_id+"@c.us" if len(chat_id) < 17 else chat_id+"@g.us"
    
        
    api_url = f"https://api.green-api.com/waInstance{instanceId}/sendMessage/{api_token}"
    payload = {
            "chatId": chat_id,
            "message": msg
        }

    response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json = payload)
    
    if not response.ok:
        data = {'code': response.status_code, 'content': response.text}
        return jsonify(data)
    print(chat_id+'dddd')
    data = response.json()
    return jsonify(data)



@app.route('/sendFileByUrl', methods=['POST'])
def send_file():
    instanceId = flaskRequest.args.get('instanceId')
    api_token = flaskRequest.args.get('apiInstanceToken')
    data = flaskRequest.get_json()
    url = data.get('urlFile')
    caption = data.get('caption')
    fileName = data.get('fileName')
    chat_id = data.get('chatId')
    chat_id = chat_id+"@c.us" if len(chat_id) < 17 else chat_id+"@g.us"     
    
    api_url = f"https://api.green-api.com/waInstance{instanceId}/sendFileByUrl/{api_token}"
    payload = {
            "chatId": chat_id,
            "urlFile": url,
            "caption": caption,
            "fileName": fileName
        }

    response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json = payload)
    
    if not response.ok:
        data = {'code': response.status_code, 'content': response.text}
        return jsonify(data)

    data = response.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
