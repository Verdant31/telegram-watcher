import os
from dotenv import load_dotenv
from telethon import TelegramClient


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
        self.notification_chat_id = os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID")

    def _validate_env_vars(self):
        """Verifica se todas as variáveis de ambiente foram carregadas"""
        required_vars = [
            ("TELEGRAM_API_ID", self.api_id),
            ("TELEGRAM_API_HASH", self.api_hash),
            ("TELEGRAM_SESSION", self.session_file)
        ]

        missing_vars = []
        for var_name, var_value in required_vars:
            if not var_value or var_value == "None":
                missing_vars.append(var_name)

        if missing_vars:
            raise ValueError(
                f"❌ Variáveis de ambiente não encontradas: {', '.join(missing_vars)}")

        # Validação especial para TELEGRAM_NOTIFICATION_CHAT_ID (pode ser vazia inicialmente)
        if not self.notification_chat_id:
            print("⚠️  TELEGRAM_NOTIFICATION_CHAT_ID não configurado. Use o comando /get_chat_id para obter seu ID.")

        print("✅ Todas as variáveis de ambiente carregadas com sucesso!")

    def create_telegram_client(self):
        """Cria e retorna o cliente do Telegram"""
        return TelegramClient(self.session_file, self.api_id, self.api_hash)
