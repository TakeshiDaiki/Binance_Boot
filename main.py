import time
import sys
from datetime import datetime
import config
from core.exchange import get_connection, fetch_data, place_order
from logic.indicators import add_indicators
from logic.strategy import generate_signal


def run_bot():
    print("\n" + "=" * 45)
    print("🚀 PANTUFLITO-BOT: TRADING SYSTEM ACTIVE")
    print("=" * 45)

    print("1. DEMO | 2. REAL")
    option = input("Select execution mode: ")
    is_demo = True if option == "1" else False

    exchange = get_connection(use_demo=is_demo)

    in_position = False
    active_side = None

    try:
        while True:
            try:
                df = fetch_data(exchange, config.SYMBOL, config.TIMEFRAME)
                if df.empty:
                    time.sleep(10)
                    continue

                df = add_indicators(df)
                last_price = df['close'].iloc[-1]
                signal = generate_signal(df)

                timestamp = datetime.now().strftime('%H:%M:%S')
                print(f"[{timestamp}] {config.SYMBOL}: {last_price} | Signal: {signal} | In Position: {in_position}")

                # Entry Logic
                if signal != 'HOLD' and not in_position:
                    print(f"🎯 Signal detected. Opening {signal}...")
                    order = place_order(exchange, config.SYMBOL, signal, config.QUANTITY)
                    if order:
                        in_position = True
                        active_side = signal
                        print(f"✅ Order executed successfully.")

                # Exit Logic
                elif in_position and signal != 'HOLD' and signal != active_side:
                    print(f"🏁 Closing {active_side} position...")
                    closing_side = 'sell' if active_side == 'LONG' else 'buy'
                    if place_order(exchange, config.SYMBOL, closing_side, config.QUANTITY):
                        in_position = False
                        active_side = None
                        print(f"✅ Position closed.")

                time.sleep(60)

            except Exception as e:
                print(f"⚠️ Runtime Error: {e}")
                time.sleep(15)

    except KeyboardInterrupt:
        print("\n👋 Stopping the bot...")
        sys.exit()


if __name__ == "__main__":
    run_bot()