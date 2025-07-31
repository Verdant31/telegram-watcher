#!/usr/bin/env python3
"""
Script auxiliar para obter o Chat ID do Telegram
Execute este script e envie uma mensagem para o bot para obter seu Chat ID
"""

from telethon import events
from config import MonitorConfig

config = MonitorConfig()
client = config.create_telegram_client()


@client.on(events.NewMessage())
async def handler(event):
    """Handler para capturar mensagens e mostrar o chat ID"""
    chat_id = event.chat_id
    user = await event.get_sender()

    print(f"\nChat ID encontrado: {chat_id}")
    print(f"Usuário: {user.first_name}", end="")
    if user.last_name:
        print(f" {user.last_name}", end="")
    if user.username:
        print(f" (@{user.username})", end="")

    print(f"\nAdicione esta linha ao seu arquivo .env:")
    print(f"TELEGRAM_NOTIFICATION_CHAT_ID={chat_id}")

    response = f"✅Seu Chat ID é: `{chat_id}`\n"
    response += f" Adicione esta linha ao seu arquivo .env:\n"
    response += f"`TELEGRAM_NOTIFICATION_CHAT_ID={chat_id}`\n\n"

    await event.reply(response)

    print(f"\nScript finalizado. Chat ID configurado!")
    client.disconnect()


if __name__ == "__main__":
    print("Script para obter Chat ID iniciado!")
    print("Envie qualquer mensagem para o seu bot para obter seu Chat ID")

    try:
        client.start()
        client.run_until_disconnected()
    except KeyboardInterrupt:
        print("\n👋 Script interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
