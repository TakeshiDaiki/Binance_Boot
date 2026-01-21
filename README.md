# Pantuflito-Bot - Automated Trading System

A production-ready, automated trading bot featuring real-time market data analysis, 
comprehensive technical indicator integration, and enterprise-level architecture. 
Built with Python 3.10+, CCXT, and Pandas.

🚀 Features

Authentication & Security

✅ API Key-based authentication for Binance integration
✅ Secure environment variable management via .env
✅ Automated .gitignore configuration for credential protection
✅ Built-in CCXT rate limiting for exchange safety
✅ Protected fallback mechanisms for environment loading

Core Functionality

✅ Real-time market data fetching (OHLCV)
✅ EMA 50/200 Trend filtering logic
✅ RSI 50-level crossover momentum trigger
✅ Volume-based signal confirmation
✅ Automated position tracking and state management
✅ 1:2 Risk/Reward ratio execution (TP 1.5% / SL 0.75%)

Developer Experience

✅ Modular architecture (Core / Logic / Config)
✅ PEP 8 compliant code structure
✅ Vectorized data processing with Pandas
✅ Comprehensive logging and real-time console feedback
✅ Centralized configuration management

🛠️ Tech Stack

Backend

Runtime: Python 3.10+
Exchange Library: CCXT
Data Analysis: Pandas
Environment: Python-Dotenv
Market: Binance (Live & Testnet)

DevOps

Version Control: Git & GitHub
Configuration: .env management
Dependencies: pip (requirements.txt)

📦 Installation

Prerequisites

Python 3.10+ and pip
Binance API Keys (Real or Testnet)

Quick Start

# Clone the repository
git clone https://github.com/TakeshiDaiki/Binance_Boot.git
cd Binance_Boot

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your Binance API Keys

# Run the application
python main.py

🔧 Environment Variables

Binance Credentials (.env)

REAL_API_KEY=your_real_api_key_here
REAL_SECRET_KEY=your_real_secret_key_here

DEMO_API_KEY=your_testnet_api_key_here
DEMO_SECRET_KEY=your_testnet_secret_key_here

📚 Strategy Documentation

The bot implements a trend-following momentum strategy:

Key Logic

Method          Condition               Description
EMA Filter      EMA 50 > EMA 200        Uptrend Filter (Longs only)
EMA Filter      EMA 50 < EMA 200        Downtrend Filter (Shorts only)
RSI Trigger     Crossover 50            Momentum confirmation
Volume Check    Current > Avg(20)       Liquidity validation
Take Profit     Price + 1.5%            Automated exit (Gain)
Stop Loss       Price - 0.75%           Automated exit (Risk)

📁 Project Structure

Binance_Boot/
├── core/
│   ├── exchange.py      # Connection logic & Order execution
│   └── risk.py          # Risk management parameters
├── logic/
│   ├── indicators.py    # Technical indicators (EMA, RSI, Volume)
│   └── strategy.py      # Signal generation logic
├── config.py            # Global configuration & symbols
├── main.py              # Entry point & execution loop
├── .env                 # Private credentials (ignored)
├── .env.example         # Template for other developers
├── .gitignore           # Version control security rules
├── requirements.txt     # Dependency manifest
└── README.md            # Project documentation

🤝 Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

📝 Scripts Reference

Script                  Description
python main.py          Starts the main trading loop
pip install -r reqs.txt Installs all necessary libraries
python -m pip --upgrade Updates project dependencies

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author

Jose Salazar
GitHub: https://github.com/TakeshiDaiki
LinkedIn: https://www.linkedin.com/in/jose-salazar-60ab21283/

🙏 Acknowledgments

CCXT team for the robust exchange library
Pandas community for the data processing tools
Binance for the comprehensive API documentation

Note: This is a portfolio/demonstration project. 
For production use, ensure proper risk assessment and monitoring are in place.
