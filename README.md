# Telegram Deal Monitor

A Python application that monitors Telegram messages for specific keywords and sends notifications via Telegram when promotional deals are detected.

## Features

- Real-time Telegram message monitoring
- Keyword-based deal detection
- Telegram notifications (no external APIs required!)
- Customizable keyword list
- Secure environment variable configuration
- Docker support for easy deployment

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd telegram-watch
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env` or create a new `.env` file
   - Fill in your actual credentials (see configuration section)

4. Get your Telegram Chat ID:
```bash
python get_chat_id.py
```
   - Send any message to the bot (‼️‼️You can also send a message to your 'Saved Messages' chat on Telegram and use it to receive your notifications.)
   - Copy the Chat ID and add it to your `.env` file

5. Configure keywords in `keywords.txt`

6. Run the monitor:
```bash
python monitor.py
```

## Configuration

### Required Environment Variables

Create a `.env` file with the following variables:

- `TELEGRAM_API_ID`: Telegram API ID (get from https://my.telegram.org)
- `TELEGRAM_API_HASH`: Telegram API Hash
- `TELEGRAM_SESSION`: Session file path (default: session_data/monitor)
- `TELEGRAM_NOTIFICATION_CHAT_ID`: Your Telegram Chat ID (get using get_chat_id.py)


### Keywords Configuration

Edit the `keywords.txt` file to specify which keywords to monitor:

```txt
# Keywords for deal monitoring
# One keyword per line
# Lines starting with # are comments

ssd
graphics card
laptop
sale
discount
promoção
oferta
desconto
```

## How to Get Telegram API Credentials

1. Visit https://my.telegram.org
2. Log in with your phone number
3. Go to "API development tools"
4. Create a new application
5. Note down the `api_id` and `api_hash`

## Project Structure

```
telegram-watch/
├── config.py              # Configuration and environment setup
├── monitor.py             # Main monitoring application
├── get_my_chat_id.py      # Simple script to get your Chat ID
├── get_chat_id.py         # Alternative Chat ID helper (interactive)
├── test_notification.py   # Test script to verify notifications
├── utils.py               # Utility functions for keyword processing
├── keywords.txt           # Keywords to monitor
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Docker Compose setup
├── .env.example           # Environment variables template
└── session_data/          # Telegram session storage
```

## How It Works

1. The application connects to Telegram using the Telethon library
2. It monitors incoming messages in real-time
3. Each message is checked against the keywords in `keywords.txt`
4. When a match is found, a Telegram notification is sent to your configured Chat ID
5. The notification includes the matched keywords and the original message

## Available Commands


When running the test script, you can use:

- `/test`: Send a test notification to verify the system is working

### Testing notification
- Run `python test_notification.py` and send `/test` in the bot chat to verify setup
- Check if the Chat ID in `.env` matches the one from `get_my_chat_id.py`
- Verify your Telegram API credentials are correct

## Docker Deployment

For Docker deployment:

1. Configure environment variables in the `.env` file (see configuration section above)

2. Run with Docker Compose:
```bash
docker-compose run --rm telegram-watcher
```

**Security Note**: The `docker-compose.yml` uses `env_file: .env` to load environment variables securely. Never put credentials directly in docker-compose.yml!

## Dependencies

- `telethon`: Telegram client library
- `python-dotenv`: Environment variable management

## Advantages over the Previous Version

- ✅ **Free**: No costs - uses Telegram for notifications
- ✅ **Simpler**: Fewer dependencies and configuration steps
- ✅ **More reliable**: Direct Telegram API without external service dependencies
- ✅ **Real-time**: Instant notifications through Telegram
- ✅ **Easy testing**: Dedicated test scripts to verify functionality

## License

This project is for educational and personal use. Please respect Telegram's terms of service.
