import config


def add_indicators(df):
    """
    Calculates technical indicators (EMA, RSI, and Average Volume)
    using the parameters defined in the config file.
    """

    # Calculate EMA (Exponential Moving Average)
    # We use .ewm directly on the 'close' column of the dataframe
    df['ema50'] = df['close'].ewm(span=config.EMA_FAST, adjust=False).mean()
    df['ema200'] = df['close'].ewm(span=config.EMA_SLOW, adjust=False).mean()

    # Calculate Manual RSI (Relative Strength Index)
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=config.RSI_PERIOD).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=config.RSI_PERIOD).mean()

    # Avoid division by zero
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))

    # Calculate Average Volume
    df['vol_avg'] = df['volume'].rolling(window=config.VOL_PERIOD).mean()

    return df