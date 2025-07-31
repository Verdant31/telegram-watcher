from telethon import events
from config import MonitorConfig
from utils import load_keywords, check_keywords_in_message

config = MonitorConfig()

keywords = load_keywords()
tw_client = config.create_twilio_client()
client = config.create_telegram_client()


@client.on(events.NewMessage())
async def handler(event):
    msg = event.message.message

    found_keywords = check_keywords_in_message(msg, keywords)

    if found_keywords:
        print(f"[MATCH FOUND] Keywords: {', '.join(found_keywords)}")
        print(f"[MESSAGE] {msg}")
        try:
            wa = tw_client.messages.create(
                body=f"🚨 Nova promoção encontrada!\n\nPalavras-chave: {', '.join(found_keywords)}\n\nMensagem: {msg}",
                from_=config.twilio_from,
                to=config.whatsapp_to
            )
            print(f"[NOTIFICATION SENT] Message SID: {wa.sid}")
        except Exception as e:
            print(f"[ERROR] Falha ao enviar notificação: {e}")
    else:
        pass

client.start()
print("🚀 Monitor de promoções iniciado!")
print(
    f"📋 Monitorando {len(keywords)} palavras-chave: {', '.join(keywords[:5])}{'...' if len(keywords) > 5 else ''}")
print("👂 Aguardando mensagens...")
client.run_until_disconnected()
