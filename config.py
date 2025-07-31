import os
from dotenv import load_dotenv
from telethon import TelegramClient
from twilio.rest import Client


class MonitorConfig:
    def __init__(self):
        load_dotenv()
        self._load_env_vars()
        self._validate_env_vars()

    def _load_env_vars(self):
        """Carrega todas as variáveis de ambiente"""
        self.api_id = int(str(os.getenv("TELEGRAM_API_ID")))
        self.api_hash = str(os.getenv("TELEGRAM_API_HASH"))
        self.session_file = os.getenv(
            "TELEGRAM_SESSION", "session_data/monitor")
        self.twilio_sid = str(os.getenv("TWILIO_SID"))
        self.twilio_token = str(os.getenv("TWILIO_TOKEN"))
        self.twilio_from = str(os.getenv("TWILIO_FROM_NUMBER"))
        self.whatsapp_to = str(os.getenv("WHATSAPP_TO_NUMBER"))

    def _validate_env_vars(self):
        """Verifica se todas as variáveis de ambiente foram carregadas"""
        required_vars = [
            ("TELEGRAM_API_ID", self.api_id),
            ("TELEGRAM_API_HASH", self.api_hash),
            ("TWILIO_SID", self.twilio_sid),
            ("TWILIO_TOKEN", self.twilio_token),
            ("TWILIO_FROM_NUMBER", self.twilio_from),
            ("WHATSAPP_TO_NUMBER", self.whatsapp_to),
            ("TELEGRAM_SESSION", self.session_file)
        ]

        missing_vars = []
        for var_name, var_value in required_vars:
            if not var_value or var_value == "None":
                missing_vars.append(var_name)

        if missing_vars:
            raise ValueError(
                f"❌ Variáveis de ambiente não encontradas: {', '.join(missing_vars)}")

        print("✅ Todas as variáveis de ambiente carregadas com sucesso!")

    def create_telegram_client(self):
        """Cria e retorna o cliente do Telegram"""
        return TelegramClient(self.session_file, self.api_id, self.api_hash)

    def create_twilio_client(self):
        """Cria e retorna o cliente do Twilio"""
        return Client(self.twilio_sid, self.twilio_token)
