#!/usr/bin/env python3
"""
Script para testar se as notificações do Telegram estão funcionando
"""
from telethon import events
from config import MonitorConfig
from utils import send_telegram_notification


async def test_notification():
    """Testa o envio de notificação para o grupo configurado"""
    config = MonitorConfig()
    if (not config.api_id or not config.api_hash):
        print(
            "❌ Variáveis de ambiente TELEGRAM_API_ID e TELEGRAM_API_HASH não configuradas.")
        return

    try:
        print("Conectando ao Telegram...")

        if not config.notification_chat_id:
            print("TELEGRAM_NOTIFICATION_CHAT_ID não configurado no .env")
            print("Execute 'python setup_group.py' para configurar automaticamente")
            return False

        print(f"Chat ID configurado: {config.notification_chat_id}")
        print("Enviando mensagem de teste para o grupo...")

        success = await send_telegram_notification(
            config.notification_chat_id,
            "Teste do sistema de notificacoes",
            "Esta e uma mensagem de teste para verificar se o sistema esta funcionando corretamente."
        )

        if success:
            print("Mensagem de teste enviada com sucesso!")
            print("Verifique o grupo 'Notificacoes de Ofertas' no Telegram")
            return True
        else:
            print("Falha ao enviar mensagem de teste")
            return False

    except Exception as e:
        print(f"Erro durante o teste: {e}")
        return False

if __name__ == "__main__":
    print("=== Teste de Notificacao ===")
    print("Este script enviara uma mensagem de teste para o grupo configurado")
    print()

    import asyncio
    success = asyncio.run(test_notification())

    if success:
        print("\nTeste concluido com sucesso!")
        print("O sistema de notificacoes esta funcionando corretamente.")
    else:
        print("\nTeste falhou!")
        print("Verifique a configuracao e tente novamente.")
