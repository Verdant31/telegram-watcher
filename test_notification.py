#!/usr/bin/env python3
"""
Script para testar se as notificações do Telegram estão funcionando
"""
from telethon import events
from config import MonitorConfig
from utils import send_telegram_notification

config = MonitorConfig()
client = config.create_telegram_client()


@client.on(events.NewMessage(pattern='/test'))
async def test_handler(event):
    """Handler para teste de notificação"""
    print("Comando /test recebido! Enviando notificação de teste...")

    if not config.notification_chat_id:
        await event.reply("TELEGRAM_NOTIFICATION_CHAT_ID não configurado no .env\n💡 Execute 'python get_my_chat_id.py' para obter seu Chat ID")
        return

    success = await send_telegram_notification(
        client,
        config.notification_chat_id,
        "Este é um teste do sistema de notificações.",
        "Mensagem de teste para verificar se o sistema está funcionando corretamente."
    )

    if success:
        await event.reply("Notificação enviada com sucesso.")
        print("Notificação enviada com sucesso.")
    else:
        await event.reply("Não foi possível enviar a notificação.")
        print("Não foi possível enviar a notificação.")

if __name__ == "__main__":
    print("Script de teste de notificação iniciado!")
    print("Envie '/test' para testar as notificações")

    client.start()

    if config.notification_chat_id:
        print(f"Chat ID configurado: {config.notification_chat_id}")
    else:
        print("Chat ID não configurado!")

    client.run_until_disconnected()
