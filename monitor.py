from telethon import events
from config import MonitorConfig
from utils import load_keywords, check_keywords_in_message, send_telegram_notification

config = MonitorConfig()
keywords = load_keywords()
client = config.create_telegram_client()

@client.on(events.NewMessage())
async def handler(event):
    """Handler principal para monitorar mensagens"""
    msg = event.message.message

    # Ignora comandos do bot
    if msg.startswith('/'):
        return

    found_keywords = check_keywords_in_message(msg, keywords)

    if found_keywords:
        print(f"[MATCH FOUND] Keywords: {', '.join(found_keywords)}")
        print(f"[MESSAGE] {msg[:100]}{'...' if len(msg) > 100 else ''}")

        # Monta a mensagem de notificação
        keywords_text = ', '.join(found_keywords)
        notification_message = f"Palavras-chave encontradas: {keywords_text}"

        # Envia notificação via Telegram
        success = await send_telegram_notification(
            client,
            config.notification_chat_id,
            notification_message,
            msg
        )

        if success:
            print(f"[NOTIFICATION SENT] ✅")
        else:
            print(f"[NOTIFICATION FAILED] ❌")



if __name__ == "__main__":
    client.start()
    print("🚀 Monitor de promoções iniciado!")
    print(
        f"📋 Monitorando {len(keywords)} palavras-chave: {', '.join(keywords[:5])}{'...' if len(keywords) > 5 else ''}")

    if config.notification_chat_id:
        print(
            f"📱 Notificações serão enviadas para o chat ID: {config.notification_chat_id}")
    else:
        print(
            "⚠️  Chat ID não configurado. Envie /get_chat_id para o bot para obter seu ID.")

    print("👂 Aguardando mensagens...")
    client.run_until_disconnected()
