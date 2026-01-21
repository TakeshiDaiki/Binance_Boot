Pantuflito-Bot - Automated Trading System

A production-ready automated trading bot featuring real-time market data analysis, technical indicator integration, and a scalable modular architecture. Built with Python 3.10+, CCXT and Pandas.

🚀 Features

🔐 Authentication & Securit

API Key-based authentication for Binance

Secure environment variable management via .env

Automated .gitignore configuration for credential protection

Built-in CCXT rate limiting

Safe environment loading with fallback mechanisms

⚙️ Core Functionality

Real-time OHLCV market data fetching

EMA 50/200 trend filtering

RSI 50-level momentum trigger

Volume-based confirmation

Automated position tracking

1:2 Risk/Reward ratio (TP 1.5% / SL 0.75%)

🧑‍💻 Developer Experience

Modular architecture (Core / Logic / Config)

PEP8-compliant structure

Vectorized data processing with Pandas

Real-time logging

Centralized configuration management

🛠️ Tech Stack
Backend

Python 3.10+

CCXT

Pandas

Binance API

DevOps

Git & GitHub

.env configuration

pip / requirements.txt

📦 Installation
Prerequisites

Python 3.10+

Binance API keys (Live or Testnet)

🚀 Quick Start

git clone https://github.com/TakeshiDaiki/Binance_Boot.git
cd Binance_Boot
pip install -r requirements.txt
cp .env.example .env
python main.py


## 🔧 Environment Variables

Create a `.env` file with the following structure:

```env
REAL_API_KEY=your_real_api_key_here
REAL_SECRET_KEY=your_real_secret_key_here
DEMO_API_KEY=your_testnet_api_key_here
DEMO_SECRET_KEY=your_testnet_secret_key_here
```

📚 Strategy Documentation

🧠 Strategy Logic
| Indicator   | Condition      | Description            |
| ----------- | -------------- | ---------------------- |
| EMA 50/200  | EMA50 > EMA200 | Long trend filter      |
| EMA 50/200  | EMA50 < EMA200 | Short trend filter     |
| RSI         | Crosses 50     | Momentum trigger       |
| Volume      | > Avg(20)      | Liquidity confirmation |
| Take Profit | +1.5%          | Exit in profit         |
| Stop Loss   | -0.75%         | Risk control           |

## 📁 Project Structure

```text
Binance_Boot/
├── core/
│   ├── exchange.py
│   └── risk.py
├── logic/
│   ├── indicators.py
│   └── strategy.py
├── config.py
├── main.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

🤝 Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to your branch

Open a Pull Request

Scripts Reference
| Command                             | Description             |
| ----------------------------------- | ----------------------- |
| python main.py                      | Starts the trading loop |
| pip install -r requirements.txt     | Install dependencies    |
| python -m pip install --upgrade pip | Upgrade pip             |

📄 License

This project is licensed under the MIT License.

👤 Author

Jose Salazar

GitHub: https://github.com/TakeshiDaiki

LinkedIn: https://www.linkedin.com/in/jose-salazar-60ab21283/

⚠️ Important Note

This is a demonstration and portfolio project.
The strategy is functional, but the bot is provided as a test and showcase system only.
It is not recommended to operate it in real trading environments without further validation, auditing and risk management.

🙏 Acknowledgments

CCXT team for the exchange library

Pandas community for data processing tools

Binance for the API documentation


