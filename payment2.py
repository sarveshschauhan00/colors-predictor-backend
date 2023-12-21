import json
import requests
import time
import hashlib

# Binance Pay API endpoint
api_url = "https://api.binance.com/binancepay/openapi/v2/order"

# Your Binance Pay API key and secret key
api_key = "3eae5afb61a1e994faa27930e7b12abd3278e6e6c9814e89eae997090b85a017"
secret_key = "scjyqob9u2evokco9senagdkveor7k3z1e976y8u2uuyfjhwzlue1acxk9thgbbc"

# Construct the request payload
payload = {
    "env": {
        "terminalType": "WEB"
    },
    "orderTags": {
        "ifProfitSharing": True
    },
    "merchantTradeNo": "9825382937292",
    "orderAmount": 25.17,
    "currency": "USDT",
    "goods": {
        "goodsType": "01",
        "goodsCategory": "D000",
        "referenceGoodsId": "7876763A3B",
        "goodsName": "Ice Cream",
        "goodsDetail": "Greentea ice cream cone"
    }
}

# Get the current timestamp
timestamp = int(time.time() * 1000)

# Calculate the signature
payload_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
signature_payload = f"{payload_json}{secret_key}"
signature = hashlib.sha256(signature_payload.encode("utf-8")).hexdigest()

# Set up headers
headers = {
    "Content-Type": "application/json",
    "X-Binance-PAY-APIKEY": api_key,
    "X-Binance-PAY-SIGNATURE": signature,
    "X-Binance-PAY-TIMESTAMP": str(timestamp)
}

# Make the API request
response = requests.post(api_url, json=payload, headers=headers)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print("API Response:")
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
