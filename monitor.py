from telethon import events
from config import MonitorConfig
from utils import load_keywords, check_keywords_in_message, send_telegram_notification
import signal
import sys
import asyncio
from telethon import TelegramClient

config = MonitorConfig()
config._validate_env_vars()

groups_keywords = load_keywords()


user_client = TelegramClient(config.session_file,
                             config.api_id, config.api_hash)
bot_client = TelegramClient(config.bot_session_file,
                            config.api_id, config.api_hash)


def signal_handler(sig, frame):
    """Handler para fechar conexões ao receber sinal de interrupção"""
    print("\n🔄 Encerrando monitor e fechando conexões...")
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.close()
    except:
        pass
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


@user_client.on(events.NewMessage())
async def handler(event):
    """Handler principal para monitorar mensagens"""
    msg = event.message.message

    if msg.startswith('/'):
        return

    chat = await event.get_chat()
    chat_title = getattr(chat, 'title', 'Chat Privado')

    matched_group = None
    keywords_to_check = []

    for group_name in groups_keywords.keys():
        if group_name.lower() in chat_title.lower():
            matched_group = group_name
            keywords_to_check = groups_keywords[group_name]
            break

    if not matched_group:
        return
    print(
        f"🔍 Grupo: {matched_group} - {chat_title}, Message: {msg.split(chr(10))[0]}")
    found_keywords = check_keywords_in_message(msg, keywords_to_check)

    if found_keywords:
        print(f"[MATCH FOUND] Grupo: {matched_group}")
        print(f"[MATCH FOUND] Keywords: {', '.join(found_keywords)}")
        print(f"[MESSAGE] {msg[:100]}{'...' if len(msg) > 100 else ''}")

        keywords_text = ', '.join(found_keywords)
        notification_message = f"🎯 Grupo: {matched_group}\n📝 Palavras-chave: {keywords_text}"

        success = await send_telegram_notification(
            bot_client,
            config.notification_chat_id,
            notification_message,
            msg
        )

        if success:
            print(f"[NOTIFICATION SENT] Enviado")
        else:
            print(f"[NOTIFICATION FAILED] Falhou")


async def main():
    await user_client.start()  # type: ignore
    await bot_client.start(bot_token=config.bot_token)  # type: ignore

    total_groups = len(groups_keywords)
    total_keywords = sum(len(words) for words in groups_keywords.values())

    print(
        f"Monitorando {total_groups} grupos com {total_keywords} palavras-chave:")
    for group_name, words in groups_keywords.items():
        words_preview = ', '.join(words[:3])
        if len(words) > 3:
            words_preview += f"... (+{len(words)-3})"
        print(f"  📁 {group_name}: {words_preview}")

    if config.notification_chat_id:
        print(
            f"Notificacoes serao enviadas para o chat ID: {config.notification_chat_id}")
    else:
        print("Chat ID nao configurado. Execute 'python setup_group.py' para configurar automaticamente.")

    print("Aguardando mensagens...")
    try:
        tasks = [
            user_client.run_until_disconnected(),
            bot_client.run_until_disconnected(),
        ]

        await asyncio.gather(*tasks)  # type: ignore
    except KeyboardInterrupt:
        print("\n🔄 Encerrando monitor...")


if __name__ == "__main__":
    asyncio.run(main())
