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


def get_account_balance():
    url = "https://api.coindcx.com/exchange/v1/users/balances"
    payload = {}
    headers, payload_str = get_headers(payload)

    response = requests.post(url, data=payload_str, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Filter only coins with non-zero balance
        non_zero = [item for item in data if float(item["balance"]) > 0]
        return non_zero
    else:
        print("Error:", response.text)
        return []

def get_market_data(symbol="BTCINR"):
    """
    Fetch real-time ticker data from CoinDCX for the given symbol.
    """
    url = f"https://public.coindcx.com/market_data/ticker"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Filter for the specific trading pair (like BTCINR)
        filtered = [item for item in data if item["market"] == symbol]
        return filtered[0] if filtered else None
    else:
        print("Failed to fetch market data:", response.text)
        return None

