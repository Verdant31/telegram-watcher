#!/usr/bin/env python3
"""
Script para criar automaticamente um grupo de notificações e configurar o .env
"""
from telethon.tl.functions.messages import CreateChatRequest, AddChatUserRequest
from config import MonitorConfig
from utils import insert_chat_id_into_env
from utils import update_env_variable
from telethon import TelegramClient
import os


async def create_group_automatically(client):
    """Cria o grupo automaticamente"""
    group_name = "Notificacoes de Ofertas"

    await client(CreateChatRequest(
        users=[],
        title=group_name
    ))

    dialogs = await client.get_dialogs(limit=20)
    chat_id = None

    for dialog in dialogs:
        if hasattr(dialog.entity, 'title') and dialog.entity.title == group_name:
            chat_id = dialog.entity.id
            if chat_id > 0:
                chat_id = -chat_id
            break

    if not chat_id:
        raise Exception(
            f"Não foi possível encontrar o grupo '{group_name}' após a criação")

    print(f"✓ Grupo criado com sucesso! Nome: {group_name}")
    print(f"✓ ID do grupo: {chat_id}")

    insert_chat_id_into_env(chat_id)

    await client.send_message(chat_id,
                              "Grupo de notificacoes configurado automaticamente!\n"
                              "Este grupo recebera as notificacoes de ofertas detectadas.\n"
                              "Configuracao concluida com sucesso!")
    return chat_id


async def add_bot_to_group(client, chat_id, bot_username):
    """Adiciona o bot ao grupo criado"""
    try:
        bot_entity = await client.get_entity(bot_username)
        await client(AddChatUserRequest(
            chat_id=abs(chat_id),
            user_id=bot_entity,
            fwd_limit=100
        ))
        print(f"✓ Bot @{bot_username} adicionado ao grupo com sucesso!")
        return True
    except Exception as e:
        print(f"✗ Erro ao adicionar bot ao grupo: {e}")
        return False


async def create_bot_and_get_token():
    """Cria um bot no Telegram e retorna o token e username"""
    print("\n" + "="*50)
    print("CONFIGURAÇÃO DO BOT")
    print("="*50)
    print("O próximo passo é criar um bot que irá enviar as mensagens no grupo.")
    print("\nPara isso:")
    print("1. Pesquise pelo usuário @BotFather no Telegram")
    print("2. Inicie um novo chat com o BotFather")
    print("3. Siga as instruções para criar o bot")
    print("4. Após criar o bot, você terá acesso a um token de autenticação")
    print("-"*50)

    while True:
        bot_token = input("\n📋 Cole o token do bot aqui: ").strip()
        if not bot_token:
            print("⚠️  Token do bot não pode ser vazio. Tente novamente.")
            continue

        config = MonitorConfig()
        temp_client = None
        bot_username = None
        try:
            temp_client = TelegramClient(
                'bot_session', config.api_id, config.api_hash)
            await temp_client.start(bot_token=bot_token)  # type: ignore

            me = await temp_client.get_me()
            bot_username = getattr(me, 'username', None)

            temp_client.disconnect()
            print("✓ Token validado com sucesso!")
            break
        except Exception as e:
            print(f"✗ Token inválido: {e}")
            print("⚠️  Verifique o token e tente novamente.")
            if temp_client:
                try:
                    temp_client.disconnect()
                except:
                    pass
            continue

    update_env_variable('TELEGRAM_BOT_TOKEN', bot_token)

    return bot_token, bot_username


def cleanup_bot_session():
    temp_file = 'bot_session.session'
    if os.path.exists(temp_file):
        os.remove(temp_file)


def main():
    """Função principal para criar o grupo e configurar o projeto"""
    print("="*60)
    print("CONFIGURADOR AUTOMÁTICO DE GRUPO DE NOTIFICAÇÕES")
    print("="*60)

    try:
        config = MonitorConfig()
        if (not config.api_id or not config.api_hash):
            print(
                "❌ Variáveis de ambiente TELEGRAM_API_ID e TELEGRAM_API_HASH não configuradas.")
            return

        client = config.create_telegram_client()

        print("\n🔄 Conectando ao Telegram...")
        client.start()
        print("✓ Conectado com sucesso!")

        print("\n📂 Criando grupo de notificações...")
        chat_id = client.loop.run_until_complete(
            create_group_automatically(client))

        if not chat_id:
            print("✗ Falha ao criar o grupo automaticamente.")
            return

        bot_token, bot_username = client.loop.run_until_complete(
            create_bot_and_get_token())

        if not bot_token:
            print("✗ Falha ao criar o bot e obter o token.")
            return

        print(f"\n🤖 Adicionando bot @{bot_username} ao grupo...")
        bot_added = client.loop.run_until_complete(
            add_bot_to_group(client, chat_id, bot_username))

        print("\n" + "="*60)
        if bot_added:
            print("🎉 CONFIGURAÇÃO COMPLETA!")
            print("✓ Grupo criado")
            print("✓ Bot configurado")
            print("✓ Bot adicionado ao grupo")
            print("✓ Arquivo .env atualizado")
        else:
            print("⚠️  CONFIGURAÇÃO PARCIAL")
            print("✓ Grupo criado")
            print("✓ Bot configurado")
            print("✗ Bot não foi adicionado ao grupo")
            print("📝 Adicione o bot manualmente ao grupo")
        print("="*60)

    except Exception as e:
        print(f"\n✗ Erro durante a configuração: {e}")
        print("⚠️  Verifique suas credenciais e tente novamente.")
        cleanup_bot_session()

    finally:
        if 'client' in locals():
            try:
                client.disconnect()
            except:
                pass
        cleanup_bot_session()


if __name__ == "__main__":
    if os.path.exists('.env'):
        with open('.env', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'TELEGRAM_NOTIFICATION_CHAT_ID=' in content and 'TELEGRAM_BOT_TOKEN=' in content:
                print("✓ Configuração de bot já realizada.")
                exit(0)

    main()
