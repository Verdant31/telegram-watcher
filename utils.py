import os
import re
from config import MonitorConfig


def update_env_variable(variable_name, value):
    """Atualiza ou adiciona uma variável no arquivo .env"""
    env_path = '.env'

    if not os.path.exists(env_path):
        if os.path.exists('.env.example'):
            with open('.env.example', 'r', encoding='utf-8') as f:
                content = f.read()
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(f"{variable_name}=\n")

    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = rf'{variable_name}=.*'
    replacement = f'{variable_name}={value}'

    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
    else:
        content += f'\n{replacement}\n'

    with open(env_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Arquivo .env atualizado com {variable_name}: {value}")


def insert_chat_id_into_env(chat_id):
    """Atualiza o arquivo .env com o chat_id do grupo criado"""
    env_path = '.env'

    if not os.path.exists(env_path):
        if os.path.exists('.env.example'):
            with open('.env.example', 'r', encoding='utf-8') as f:
                content = f.read()
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write("TELEGRAM_API_ID=\n")
                f.write("TELEGRAM_API_HASH=\n")
                f.write("TELEGRAM_SESSION=session_data/monitor\n")
                f.write("TELEGRAM_NOTIFICATION_CHAT_ID=\n")

    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'TELEGRAM_NOTIFICATION_CHAT_ID=.*'
    replacement = f'TELEGRAM_NOTIFICATION_CHAT_ID={chat_id}'

    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
    else:
        content += f'\nTELEGRAM_NOTIFICATION_CHAT_ID={chat_id}\n'

    with open(env_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Arquivo .env atualizado com o chat_id: {chat_id}")


def load_keywords():
    """Carrega palavras-chave do arquivo keywords.txt"""
    keywords_file = "keywords.txt"
    keywords = []
    with open(keywords_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                keywords.append(line.lower())
    print(
        f"✅ Carregadas {len(keywords)} palavras-chave de {keywords_file}")
    return keywords


def check_keywords_in_message(message, keywords):
    """Verifica se alguma palavra-chave está presente na mensagem"""
    message_lower = message.lower()
    found_keywords = []

    for keyword in keywords:
        if keyword in message_lower:
            found_keywords.append(keyword)

    return found_keywords


async def send_telegram_notification(chat_id, message, original_message=None):
    """Envia uma notificação via Telegram"""
    try:
        config = MonitorConfig()
        bot_client = await config.create_bot_client()

        if not chat_id:
            print("Chat ID não configurado. Não foi possível enviar notificação.")
            return False

        notification_text = f"🚨 Nova promoção encontrada!\n\n📝 {message}"

        if original_message:
            notification_text += f"\n\n💬 Mensagem original:\n{original_message[:500]}{'...' if len(original_message) > 500 else ''}"

        await bot_client.send_message(int(chat_id), notification_text)
        print(f"✅ Notificação enviada via Telegram para chat ID: {chat_id}")
        return True
    except Exception as e:
        print(f"❌ Erro ao enviar notificação via Telegram: {e}")
        return False
