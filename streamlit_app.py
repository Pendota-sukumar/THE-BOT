import streamlit as st
from bot_engine import get_account_balance, execute_strategy

st.title("THE-BOT: CoinDCX Crypto Bot Dashboard")

st.header("Your Account Balance")
balances = get_account_balance()
if balances:
    for item in balances:
        st.write(f"**{item['currency']}**: {item['balance']}")
else:
    st.error("Failed to fetch balances.")

st.header("Choose Trading Strategy")
strategy = st.selectbox("Select your trading strategy:", [
    "Strategy 1: Buy Low, Sell High",
    "Strategy 2: Momentum Trading",
    "Strategy 3: RSI-Based Trading"
])

if st.button("Start Bot"):
    result = execute_strategy(strategy)
    st.success(result)
