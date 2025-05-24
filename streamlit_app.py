import streamlit as st
from bot_engine import create_exchange, fetch_data, decide_strategy, execute_trade

st.set_page_config(page_title="🤖 AI Crypto Trading Bot", layout="centered")
st.title("💸 AI Crypto Trading Bot with CoinDCX")

# Section: API Keys
st.header("🔐 API Configuration")
api_key = st.text_input("Enter CoinDCX API Key", type="password")
api_secret = st.text_input("Enter CoinDCX API Secret", type="password")

# Proceed if keys are provided
if api_key and api_secret:
    try:
        exchange = create_exchange(api_key, api_secret)
        st.success("✅ API connected successfully!")

        st.header("⚙️ Trading Settings")
        symbol = st.selectbox("Select Crypto Pair", ["BTC/INR", "ETH/INR", "DOGE/INR"])
        strategy = st.radio("Choose Strategy", ["1", "2", "3"])

        if st.button("▶️ Start Trading Bot"):
            with st.spinner("Analyzing market..."):
                price, high, low = fetch_data(exchange, symbol)
                decision = decide_strategy(strategy, price, high, low)
                result = execute_trade(exchange, symbol, decision)

                st.subheader("📊 Bot Decision Summary")
                st.metric("Current Price", f"₹{price}")
                st.write(f"**Strategy {strategy} Decision:** `{decision.upper()}`")
                st.success(f"🔁 Action Taken: {result}")

    except Exception as e:
        st.error(f"❌ Connection failed: {e}")
else:
    st.warning("Please enter your API credentials to continue.")
