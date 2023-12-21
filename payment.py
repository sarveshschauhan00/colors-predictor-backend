import json
import requests
import time
import hmac
import hashlib
import secrets

def generate_signature(timestamp, nonce, body, secret_key):
    # Step 1: Build the content
    payload = f"{timestamp}\n{nonce}\n{body}\n"

    # Step 2: Sign the content using HMAC-SHA512
    signature = hmac.new(secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha512).hexdigest().upper()

    return signature

def send_binance_pay_request(api_key, secret_key, amount, trade_number):

    payload = {
        "env": {
            "terminalType": "WEB"
        },
        "orderTags": {
            "ifProfitSharing": False
        },
        "merchantTradeNo": str(trade_number),
        "orderAmount": amount,
        "currency": "USDT",
        "goods": {
            "goodsType": "01",
            "goodsCategory": "D000",
            "referenceGoodsId": "7876763A3B",
            "goodsName": "Wallet Recharge"
        }
    }

    # Generate a random nonce
    nonce = secrets.token_hex(16)
    timestamp = int(time.time() * 1000)

    # Add or modify the expireTime parameter (in milliseconds)
    payload["orderExpireTime"] = timestamp + 600000  # Example: set expiration time to 10 minutes from now

    # Get the current timestamp
    timestamp = int(time.time() * 1000)
    print(timestamp)

    # Calculate the signature using HMAC-SHA512
    signature = generate_signature(timestamp, nonce, json.dumps(payload), secret_key)

    # Set up headers
    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": str(timestamp),
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": api_key,
        "BinancePay-Signature": signature
    }

    # Make the API request
    response = requests.post("https://bpay.binanceapi.com/binancepay/openapi/v2/order", json=payload, headers=headers)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        print("API Response:")
        print(json.dumps(data, indent=2))
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")

def query_order_status(api_key, secret_key, merchant_trade_no=None, prepay_id=None):
    nonce = secrets.token_hex(16)
    timestamp = int(time.time() * 1000)

    # Construct the request payload to query the order status
    payload = {
        "merchantId": api_key,  # Assuming merchantId is the same as API key
        "subMerchantId": api_key,  # Assuming subMerchantId is the same as API key
        "merchantTradeNo": merchant_trade_no,
        "prepayId": prepay_id
    }

    signature = generate_signature(timestamp, nonce, json.dumps(payload, separators=(',', ':'), sort_keys=True), secret_key)

    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": str(timestamp),
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": api_key,
        "BinancePay-Signature": signature
    }
    
    response = requests.post("https://bpay.binanceapi.com/binancepay/openapi/v2/order/query", json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("query status: ", data)
        return data
    else:
        return None


# Example usage
api_key = "ypsa71gv8lhraetqfzmcwh6ti7v7nuywqznzy3pbwdtcedgftuzdz9dzvwkmtivi"
secret_key = "scjyqob9u2evokco9senagdkveor7k3z1e976y8u2uuyfjhwzlue1acxk9thgbbc"

# # Construct the request payload
# payload = {
#     "env": {
#         "terminalType": "WEB"
#     },
#     "orderTags": {
#         "ifProfitSharing": False
#     },
#     "merchantTradeNo": "9825382937281",
#     "orderAmount": 1.0,
#     "currency": "USDT",
#     "goods": {
#         "goodsType": "01",
#         "goodsCategory": "D000",
#         "referenceGoodsId": "7876763A3B",
#         "goodsName": "Ice Cream",
#         "goodsDetail": "Greentea ice cream cone"
#     }
# }

# # Send the Binance Pay request
# response = send_binance_pay_request(api_key, secret_key, payload)

# merchant_trade_no = "9825382937281"
# prepay_id = response["data"]["prepayId"]

# for i in range(60):
#     order_status_data = query_order_status(api_key, secret_key, merchant_trade_no, prepay_id)
#     if order_status_data != None:
#         print(order_status_data)
#         break
#     time.sleep(1)


