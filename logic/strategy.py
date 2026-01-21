def generate_signal(df):
    """
    Generates trading signals based on EMA trend filter,
    RSI crossovers, and volume confirmation.
    """
    # Verify if there is enough data for the EMA200
    if len(df) < 200:
        return 'HOLD'

    current = df.iloc[-1]   # Current candle (forming or last closed)
    previous = df.iloc[-2]  # Previous candle

    # 1. Trend Filter (EMA)
    is_uptrend = current['ema50'] > current['ema200']
    is_downtrend = current['ema50'] < current['ema200']

    # 2. Volume Confirmation
    high_volume = current['volume'] > current['vol_avg']

    # 3. RSI Crossover Logic (Simplified)
    # LONG: RSI was below 50 and is now above or equal
    rsi_buy = previous['rsi'] < 50 <= current['rsi']

    # SHORT: RSI was above 50 and is now below or equal
    rsi_sell = previous['rsi'] > 50 >= current['rsi']

    # Final Signal Logic
    if is_uptrend and rsi_buy and high_volume:
        return 'LONG'

    if is_downtrend and rsi_sell and high_volume:
        return 'SHORT'

    return 'HOLD'