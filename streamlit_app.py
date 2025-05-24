import streamlit as st
from bot_engine import get_account_balance, execute_strategy, get_current_price

st.set_page_config(page_title="CoinDCX Crypto Bot", layout="centered")

st.title("🤖 CoinDCX Crypto Bot Dashboard")

st.header("📊 Your Account Balance")

balances = get_account_balance()

if balances:
    for item in balances:
        coin = item["currency"]
        bal = item["balance"]
        st.write(f"**{coin}**: {bal}")
else:
    st.error("❌ Failed to fetch balances.")

st.header("📈 Current BTC Price")
price = get_current_price("BTC/INR")
if price:
    st.success(f"Current BTC/INR Price: ₹{price}")
else:
    st.error("❌ Failed to fetch BTC price.")

st.header("⚙️ Choose Trading Strategy")

strategy = st.selectbox("Select your trading strategy:", [
    "Strategy 1: Buy Low, Sell High",
    "Strategy 2: Momentum Trading",
    "Strategy 3: RSI-Based Trading"
])

if st.button("🚀 Start Bot"):
    result = execute_strategy(strategy)
    st.success(result)
