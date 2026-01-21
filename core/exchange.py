import ccxt
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection(use_demo=True):
    """
    Configures the connection with Binance.
    The 'or ""' ensures the editor recognizes keys as strings.
    """
    if use_demo:
        api_key = os.getenv('DEMO_API_KEY') or ""
        secret = os.getenv('DEMO_SECRET_KEY') or ""
        mode_text = "🧪 DEMO MODE (Testnet)"
    else:
        api_key = os.getenv('REAL_API_KEY') or ""
        secret = os.getenv('REAL_SECRET_KEY') or ""
        mode_text = "💸 REAL MODE (Production)"

    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': secret,
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })

    if use_demo:
        exchange.set_sandbox_mode(True)

    print(f"\n✅ Successfully connected: {mode_text}")
    return exchange

def fetch_data(exchange, symbol, timeframe):
    """Fetches historical candlestick data (OHLCV)."""
    try:
        bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)
        df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return df
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return pd.DataFrame()

def place_order(exchange, symbol, side, amount):
    """Executes a market order (buy/sell)."""
    try:
        order = exchange.create_market_order(symbol, side.lower(), amount)
        return order
    except Exception as e:
        print(f"❌ Order error: {e}")
        return None