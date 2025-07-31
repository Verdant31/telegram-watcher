import os
from dotenv import load_dotenv
from telethon import TelegramClient


class MonitorConfig:
    def __init__(self):
        load_dotenv()
        self._load_env_vars()

    def _load_env_vars(self):
        """Carrega todas as variáveis de ambiente"""
        self.api_id = int(str(os.getenv("TELEGRAM_API_ID")))
        self.api_hash = str(os.getenv("TELEGRAM_API_HASH"))
        self.bot_token = str(os.getenv("TELEGRAM_BOT_TOKEN"))
        self.notification_chat_id = os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID")

        self.session_file = os.getenv(
            "TELEGRAM_SESSION", "session_data/monitor")
        self.bot_session_file = os.getenv(
            "TELEGRAM_BOT_SESSION", "session_data/bot_session")

    def _validate_env_vars(self):
        """Verifica se todas as variáveis de ambiente foram carregadas"""
        required_vars = [
            ("TELEGRAM_API_ID", self.api_id),
            ("TELEGRAM_API_HASH", self.api_hash),
            ("TELEGRAM_BOT_TOKEN", self.bot_token),
            ("TELEGRAM_NOTIFICATION_CHAT_ID", self.notification_chat_id),
        ]

        missing_vars = []
        for var_name, var_value in required_vars:
            if not var_value or var_value == "None":
                missing_vars.append(var_name)

        if (len(missing_vars) > 0 and ("TELEGRAM_BOT_TOKEN" in missing_vars or "TELEGRAM_NOTIFICATION_CHAT_ID" in missing_vars)):
            raise ValueError(
                "‼️  Execute 'python setup_group.py' para configurar o bot e o chat ID de notificações.")

        if len(missing_vars) > 0:
            raise ValueError(
                f"Variáveis de ambiente não encontradas: {', '.join(missing_vars)}")

    def create_telegram_client(self):
        """Cria e retorna o cliente do Telegram"""
        return TelegramClient(self.session_file, self.api_id, self.api_hash)

    async def create_bot_client(self):
        """Cria e retorna o cliente do bot do Telegram"""
        return await TelegramClient(self.bot_session_file, self.api_id, self.api_hash).start(bot_token=self.bot_token)  # type: ignore
