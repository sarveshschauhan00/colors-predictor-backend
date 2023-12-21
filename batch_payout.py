import json
import requests
import time
import hmac
import hashlib
import secrets

def generate_signature(timestamp, nonce, body, secret_key):
    payload = f"{timestamp}\n{nonce}\n{body}\n"
    signature = hmac.new(secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha512).hexdigest().upper()
    return signature

def get_wallet_balance():
    nonce = secrets.token_hex(16)
    timestamp = int(time.time() * 1000)
    payload = {
        "wallet": "FUNDING_WALLET",
        "currency": "USDT"
    }
    signature = generate_signature(timestamp, nonce, json.dumps(payload), secret_key)
    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": str(timestamp),
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": api_key,
        "BinancePay-Signature": signature
    }

    response = requests.post(payout_query_endpt, json=payload, headers=headers)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def create_batch_payout(request_id, batch_name, currency, total_amount, total_number, transfer_details):
    nonce = secrets.token_hex(16)
    timestamp = int(time.time() * 1000)

    payload = {
        "requestId": request_id,
        "batchName": batch_name,
        "currency": currency,
        "totalAmount": total_amount,
        "totalNumber": total_number,
        "transferDetailList": transfer_details
    }

    signature = generate_signature(timestamp, nonce, json.dumps(payload, separators=(',', ':'), sort_keys=True), secret_key)

    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": str(timestamp),
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": api_key,
        "BinancePay-Signature": signature
    }

    response = requests.post(batch_payout_endpt, json=payload, headers=headers)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    

def payout_query(api_key, secret_key, request_id):
    nonce = secrets.token_hex(16)
    timestamp = int(time.time() * 1000)

    # Construct the request payload to query the payout status
    payload = {
        "requestId": request_id,
    }

    signature = generate_signature(timestamp, nonce, json.dumps(payload, separators=(',', ':'), sort_keys=True), secret_key)

    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": str(timestamp),
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": api_key,
        "BinancePay-Signature": signature
    }

    response = requests.post(payout_query_endpt, json=payload, headers=headers)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    

# Replace with your actual Binance Pay API credentials
api_key = "ypsa71gv8lhraetqfzmcwh6ti7v7nuywqznzy3pbwdtcedgftuzdz9dzvwkmtivi"
secret_key = "scjyqob9u2evokco9senagdkveor7k3z1e976y8u2uuyfjhwzlue1acxk9thgbbc"

batch_payout_endpt = "https://bpay.binanceapi.com/binancepay/openapi/payout/transfer"
payout_query_endpt = "https://bpay.binanceapi.com/binancepay/openapi/balance"
payout_query_endpt = "https://bpay.binanceapi.com/binancepay/openapi/payout/query"



# Example usage
request_id = "123qweasdzxc"
batch_name = "sample_batch1"
currency = "USDT"
total_amount = 1.0
total_number = 1

transfer_details = [
    {
        "merchantSendId": "22231313131",
        "receiveType": "BINANCE_ID",
        "receiver": "511967548",
        "transferAmount": 1.0,
        "transferMethod": "FUNDING_WALLET",
        "remark": "test1"
    }
]

# response_data = create_batch_payout(request_id, batch_name, currency, total_amount, total_number, transfer_details)

# if response_data:
#     print("Batch Payout Response:")
#     print(json.dumps(response_data, indent=2))
# else:
#     print("Error creating batch payout.")


payout_query_data = payout_query(api_key, secret_key, request_id)

if payout_query_data:
    print("Payout Query Status:", payout_query_data.get("status"))
    print("Payout Query Data:", json.dumps(payout_query_data.get("data"), indent=2))
else:
    print("Error querying payout status.")

# get_wallet_balance()