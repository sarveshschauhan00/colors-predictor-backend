from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
from datetime import datetime
from payment import send_binance_pay_request, api_key, secret_key

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/api/post_example', methods=['POST'])
def post_example():
    try:
        # Get data from the POST request
        data = request.get_json()
        print(data)
        # Assuming the JSON data has a 'message' key
        message = data.get('message')
        received_time = data.get('time')
        print(received_time)

        # Get the current time
        system_current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yr, mo, da, hr, mi, se = datetime.now().strftime("%Y %m %d %H %M %S").split()
        print(system_current_time)
        # print(hr, mi, se)
        period = int(((int(hr)*3600 + int(mi)*60 + int(se)) / 60) // 3)
        extra_sec = (int(mi)%3) * 60 + int(se)
        print(yr + mo + da + str(period), (180-extra_sec)//60, (180-extra_sec)%60)
        # Process the data or perform any required operation
        # In this example, just returning the received message
        result = {'result': f'Received message: {message}'}

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/recharge', methods=['POST'])
def recharge_wallet():
    try:
        # Get data from the POST request
        data = request.get_json()
        print(data)
        response = send_binance_pay_request(api_key, secret_key, int(data["amount"]), 9825382937287)
        return jsonify(response)
        # return data

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, this is your Flask API!'}

    # Get the current time
    system_current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    yr, mo, da, hr, mi, se = datetime.now().strftime("%Y %m %d %H %M %S").split()
    print(system_current_time)
    # print(hr, mi, se)
    period = int(((int(hr)*3600 + int(mi)*60 + int(se)) / 60) // 3)
    extra_sec = (int(mi)%3) * 60 + int(se)

    return jsonify(180 - extra_sec)
    
def checkValidity():
    pass

def checkBalance():
    pass

def cerdit():
    pass

def play():
    pass

def fetch_past_records():
    pass

def fetch_user_records():
    pass

def update_past_record():
    pass

def update_user_record():
    pass



if __name__ == '__main__':
    app.run(debug=True)