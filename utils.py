import os
import re
from config import MonitorConfig


def update_env_variable(variable_name, value):
    """Atualiza ou adiciona uma variável no arquivo .env"""
    env_path = '.env'
    try:
        if not os.path.exists(env_path):
            if os.path.exists('.env.example'):
                with open('.env.example', 'r', encoding='utf-8') as f:
                    content = f.read()
                with open(env_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"📄 Arquivo .env criado a partir do .env.example")
            else:
                with open(env_path, 'w', encoding='utf-8') as f:
                    f.write(f"{variable_name}=\n")
                print(
                    f"📄 Arquivo .env criado com variável inicial: {variable_name}")

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

        print(f"✅ Arquivo .env atualizado com {variable_name}: {value}")

    except Exception as e:
        print(f"❌ Erro ao atualizar arquivo .env: {e}")
        raise


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
    """Carrega palavras-chave do arquivo keywords.txt organizadas por grupos"""
    keywords_file = "keywords.txt"
    groups_keywords = {}
    current_group = None

    with open(keywords_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                current_group = line[1:-1]  # Remove os colchetes
                groups_keywords[current_group] = []
                continue
            if current_group:
                groups_keywords[current_group].append(line.lower())

    total_keywords = sum(len(words) for words in groups_keywords.values())
    print(
        f"✅ Carregados {len(groups_keywords)} grupos com {total_keywords} palavras-chave")

    for group, words in groups_keywords.items():
        print(f"   📁 {group}: {len(words)} palavras")

    return groups_keywords


def check_keywords_in_message(message, keywords_for_group):
    """Verifica se alguma palavra-chave está presente na mensagem para um grupo específico"""
    if not keywords_for_group:
        return []

    message_lower = message.lower()
    found_keywords = []

    for keyword in keywords_for_group:
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
