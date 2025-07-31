
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


async def send_telegram_notification(client, chat_id, message, original_message=None):
    """Envia uma notificação via Telegram"""
    try:
        if not chat_id:
            print("Chat ID não configurado. Não foi possível enviar notificação.")
            return False

        notification_text = f"🚨 Nova promoção encontrada!\n\n📝 {message}"

        if original_message:
            notification_text += f"\n\n💬 Mensagem original:\n{original_message[:500]}{'...' if len(original_message) > 500 else ''}"

        await client.send_message(int(chat_id), notification_text)
        print(f"✅ Notificação enviada via Telegram para chat ID: {chat_id}")
        return True
    except Exception as e:
        print(f"❌ Erro ao enviar notificação via Telegram: {e}")
        return False
