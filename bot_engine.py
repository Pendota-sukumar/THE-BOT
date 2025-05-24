import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

import streamlit as st

API_KEY = st.secrets["coindcx"]["api_key"]
API_SECRET = st.secrets["coindcx"]["api_secret"]


exchange = ccxt.coindcx({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

def get_account_balance():
    try:
        balance = exchange.fetch_balance()
        # return list of currencies and balances
        balances = []
        for currency, info in balance['total'].items():
            if info > 0:
                balances.append({"currency": currency, "balance": info})
        return balances
    except Exception as e:
        print("Error fetching balances:", e)
        return None

# Strategy examples (mocked)
def run_strategy_1():
    return "Executed Strategy 1: Buy Low, Sell High"

def run_strategy_2():
    return "Executed Strategy 2: Momentum Trading"

def run_strategy_3():
    return "Executed Strategy 3: RSI-Based Trading"

def execute_strategy(name: str):
    if "1" in name:
        return run_strategy_1()
    elif "2" in name:
        return run_strategy_2()
    elif "3" in name:
        return run_strategy_3()
    else:
        return "Invalid Strategy"

if __name__ == "__main__":
    print("API_KEY loaded:", API_KEY is not None)
    print("API_SECRET loaded:", API_SECRET is not None)
    print("Balances:", get_account_balance())
