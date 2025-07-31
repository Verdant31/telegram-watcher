# Telegram Watch

A Python application that monitors Telegram messages for specific keywords and sends WhatsApp notifications via Twilio when promotional deals are detected.

## Features

- Real-time Telegram message monitoring
- Keyword-based deal detection
- WhatsApp notifications via Twilio API
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
   - Copy `.env.example` to `.env`
   - Fill in your actual credentials:

```bash
cp .env.example .env
```

4. Configure keywords in `keywords.txt`

5. Run the monitor:
```bash
python monitor.py
```

## Configuration

### Required Environment Variables

Create a `.env` file with the following variables:

- `TELEGRAM_API_ID`: Telegram API ID (get from https://my.telegram.org)
- `TELEGRAM_API_HASH`: Telegram API Hash
- `TELEGRAM_SESSION`: Session file path (default: session_data/monitor)
- `TWILIO_SID`: Twilio Account SID
- `TWILIO_TOKEN`: Twilio Authentication Token
- `TWILIO_FROM_NUMBER`: Your Twilio WhatsApp number (format: whatsapp:+1234567890)
- `WHATSAPP_TO_NUMBER`: Destination WhatsApp number (format: whatsapp:+1234567890)

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
```

## How to Get Credentials

### Telegram API Credentials
1. Visit https://my.telegram.org
2. Log in with your phone number
3. Go to "API development tools"
4. Create a new application
5. Note down the `api_id` and `api_hash`

### Twilio Credentials
1. Create an account at https://www.twilio.com
2. Access the Console Dashboard
3. Note down the `Account SID` and `Auth Token`
4. Set up a WhatsApp Business API number

## Project Structure

```
telegram-watch/
├── config.py           # Configuration and environment setup
├── monitor.py          # Main monitoring application
├── utils.py            # Utility functions for keyword processing
├── keywords.txt        # Keywords to monitor
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Docker Compose setup
└── session_data/       # Telegram session storage
```

## Docker Deployment

For Docker deployment:

1. Configure environment variables in the `.env` file (see configuration section above)

2. Run with Docker Compose:
```bash
docker-compose run --rm telegram-watcher
```

**Security Note**: The `docker-compose.yml` uses `env_file: .env` to load environment variables securely. Never put credentials directly in docker-compose.yml!

## How It Works

1. The application connects to Telegram using the Telethon library
2. It monitors incoming messages in real-time
3. Each message is checked against the keywords in `keywords.txt`
4. When a match is found, a WhatsApp notification is sent via Twilio
5. The notification includes the matched keywords and the original message

## Dependencies

- `telethon`: Telegram client library
- `twilio`: Twilio API client
- `python-dotenv`: Environment variable management

## License

This project is for educational and personal use. Please respect Telegram's and Twilio's terms of service.
