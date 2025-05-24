import streamlit as st
from bot_engine import get_account_balance

st.title("CoinDCX Crypto Bot Dashboard")

st.header("Your Account Balance")

balances = get_account_balance()

if balances:
    for item in balances:
        coin = item["currency"]
        bal = item["balance"]
        st.write(f"**{coin}**: {bal}")
else:
    st.error("Failed to fetch balances.")

st.header(" Choose Trading Strategy")

strategy = st.selectbox("Select your trading strategy:", [
    "Strategy 1: Buy Low, Sell High",
    "Strategy 2: Momentum Trading",
    "Strategy 3: RSI-Based Trading"
])

if st.button(" Start Bot"):
    st.success(f"Bot started with {strategy}")
    # You can call your bot logic here (we'll add this in the next step)

st.header(" Choose Trading Strategy")

strategy = st.selectbox("Select your trading strategy:", [
    "Strategy 1: Buy Low, Sell High",
    "Strategy 2: Momentum Trading",
    "Strategy 3: RSI-Based Trading"
])

if st.button(" Start Bot"):
    st.success(f"Bot started with {strategy}")
    # You can call your bot logic here (we'll add this in the next step)
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

from bot_engine import execute_strategy  # Add this at top

# Inside if st.button(" Start Bot"):
if st.button(" Start Bot"):
    result = execute_strategy(strategy)
    st.success(result)

