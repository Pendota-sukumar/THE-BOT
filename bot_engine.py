import ccxt

def create_exchange(api_key, api_secret):
    return ccxt.coindcx({
        'apiKey': api_key,
        'secret': api_secret
    })

def fetch_data(exchange, symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last'], ticker['high'], ticker['low']

def decide_strategy(strategy, price, high, low):
    if strategy == "1":
        return 'buy' if price < low + (high - low) * 0.3 else 'hold'
    elif strategy == "2":
        return 'sell' if price > low + (high - low) * 0.7 else 'hold'
    elif strategy == "3":
        return 'buy' if price < (high + low) / 2 else 'sell'
    else:
        return 'hold'

def execute_trade(exchange, symbol, action):
    if action == 'buy':
        return "Simulated BUY order executed."
    elif action == 'sell':
        return "Simulated SELL order executed."
    else:
        return "No action taken."
