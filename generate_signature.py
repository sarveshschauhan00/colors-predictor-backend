import hashlib
import hmac

def generate_signature(timestamp, nonce, body, secret_key):
    # Step 1: Build the content
    payload = f"{timestamp}\n{nonce}\n{body}\n"

    # Step 2: Sign the content using HMAC-SHA512
    signature = hmac.new(secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha512).hexdigest().upper()

    return signature

# Example usage
timestamp = "1609459200000"  # Replace with your actual timestamp
nonce = "random_nonce"      # Replace with your actual nonce
body = '{"example": "request_body"}'  # Replace with your actual request body
secret_key = "your_secret_key"        # Replace with your actual secret key

generated_signature = generate_signature(timestamp, nonce, body, secret_key)
print("Generated Signature:", generated_signature)