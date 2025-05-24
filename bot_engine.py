import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_headers(payload: dict):
    payload_str = str(payload).replace("'", '"')  # Convert dict to JSON string
    signature = hmac.new(
        bytes(API_SECRET, 'utf-8'),
        msg=bytes(payload_str, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': API_KEY,
        'X-AUTH-SIGNATURE': signature
    }
    return headers, payload_str
