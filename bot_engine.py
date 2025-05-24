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

def place_order(side, market="btcinr", quantity=0.001, price=None, order_type="limit"):
    """
    Place an order on CoinDCX.
    side: "buy" or "sell"
    market: trading pair like "btcinr"
    quantity: amount of coin to buy/sell
    price: limit price, if order_type is limit
    order_type: "limit" or "market"
    """
    url = "https://api.coindcx.com/exchange/v1/orders"
    order = {
        "side": side,
        "market": market,
        "order_type": order_type,
        "price": str(price) if price else None,
        "quantity": str(quantity),
        "recv_window": 5000,
        "timestamp": int(time.time() * 1000)
    }

    # Remove price if market order
    if order_type == "market":
        order.pop("price", None)

    headers, payload_str = get_headers(order)

    response = requests.post(url, data=payload_str, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


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


import requests
import time
import hmac
import hashlib
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# ✅ 1. Authentication headers function
def get_headers(payload):
    payload_str = json.dumps(payload, separators=(',', ':'))
    signature = hmac.new(
        API_SECRET.encode(), payload_str.encode(), hashlib.sha256
    ).hexdigest()

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': API_KEY,
        'X-AUTH-SIGNATURE': signature
    }
    return headers, payload_str

# ✅ 2. Balance fetch function
def get_account_balance():
    url = "https://api.coindcx.com/exchange/v1/users/balances"
    payload = {}
    headers, payload_str = get_headers(payload)

    response = requests.post(url, data=payload_str, headers=headers)
    if response.status_code == 200:
        data = response.json()
        non_zero = [item for item in data if float(item["balance"]) > 0]
        return non_zero
    else:
        print("Error:", response.text)
        return []

# ✅ 3. Market data fetch function
def get_market_data(symbol="BTCINR"):
    url = f"https://public.coindcx.com/market_data/ticker"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered = [item for item in data if item["market"] == symbol]
        return filtered[0] if filtered else None
    else:
        print("Failed to fetch market data:", response.text)
        return None

# ✅ 4. Strategy 1 - Real-time example
def run_strategy_1():
    data = get_market_data("BTCINR")
    if not data:
        return "Failed to fetch BTC market data."

    price = float(data['last_price'])
    low = float(data['low'])
    high = float(data['high'])

    if price <= low * 1.01:
        return f"🔽 BTC Price: ₹{price} is near day’s low ({low}). Consider buying."
    elif price >= high * 0.99:
        return f"🔼 BTC Price: ₹{price} is near day’s high ({high}). Consider selling."
    else:
        return f"ℹ️ BTC Price: ₹{price} - No action triggered."

# ✅ 5. Dummy strategies (can be upgraded later)
def run_strategy_2():
    return "Executed Strategy 2: Momentum Trading"

def run_strategy_3():
    return "Executed Strategy 3: RSI-Based Trading"

# ✅ 6. Selector
def execute_strategy(name: str):
    if "1" in name:
        return run_strategy_1()
    elif "2" in name:
        return run_strategy_2()
    elif "3" in name:
        return run_strategy_3()
    else:
        return "Invalid Strategy"
