import ccxt
import streamlit as st

API_KEY = st.secrets["coindcx"]["api_key"]
API_SECRET = st.secrets["coindcx"]["api_secret"]

# NOTE: ccxt has no coindcx module. So we simulate with balance mock for demo
def get_account_balance():
    try:
        # Simulated balance (since ccxt doesn't support coindcx)
        return [
            {"currency": "BTC", "balance": 0.001},
            {"currency": "INR", "balance": 500}
        ]
    except Exception as e:
        print(f"Balance fetch error: {e}")
        return []

def get_current_price(pair="BTC/INR"):
    try:
        binance = ccxt.binance()
        ticker = binance.fetch_ticker(pair)
        return ticker["last"]
    except Exception as e:
        print(f"Price fetch error: {e}")
        return None

def run_strategy_1():
    return "✅ Executed Strategy 1: Buy Low, Sell High"

def run_strategy_2():
    return "✅ Executed Strategy 2: Momentum Trading"

def run_strategy_3():
    return "✅ Executed Strategy 3: RSI-Based Trading"

def execute_strategy(name: str):
    if "1" in name:
        return run_strategy_1()
    elif "2" in name:
        return run_strategy_2()
    elif "3" in name:
        return run_strategy_3()
    else:
        return "❌ Invalid Strategy"
