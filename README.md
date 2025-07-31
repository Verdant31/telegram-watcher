# Monitor de Ofertas Telegram

Um aplicativo Python que monitora mensagens do Telegram em tempo real, detecta ofertas baseadas em palavras-chave e envia notificações automáticas.

## 🎯 O que faz este projeto?

- **Monitora** todas as mensagens que você recebe no Telegram
- **Detecta** ofertas quando palavras-chave específicas aparecem
- **Notifica** você instantaneamente através de um bot
- **Funciona** 24/7 em segundo plano

## ⚡ Recursos Principais

- ✅ Monitoramento em tempo real de mensagens do Telegram
- ✅ Sistema de detecção por palavras-chave personalizáveis  
- ✅ Notificações via bot do Telegram (alertas reais no celular)
- ✅ Configuração automática de grupo de notificações
- ✅ Suporte ao Docker para deploy
- ✅ Interface simples e scripts automatizados

## 🚀 Configuração Rápida (5 minutos)

### Passo 1: Preparação do Ambiente

```bash
# Clone o repositório
git clone <repository-url>
cd ofertas-adrenaline

# Instale as dependências
pip install -r requirements.txt
```

### Passo 2: Obtenha Credenciais da API do Telegram

1. Acesse: https://my.telegram.org
2. Faça login com seu número de telefone
3. Vá em "API development tools"
4. Crie uma nova aplicação
5. **Guarde:** `api_id` e `api_hash`

### Passo 3: Crie um grupo e configure o bot que irá alertar

Foi criado um arquivo para te ajudar a configurar o grupo, basta executar:
```bash
python setup_group.py
```


**Este script irá:**
- Conectar ao Telegram com suas credenciais
- Criar um grupo chamado "Notificacoes de Ofertas"
- Atualizar automaticamente o `.env` com o ID do grupo
- Adicionar o bot ao grupo
- Enviar uma mensagem de confirmação

### Passo 4: Configure o Arquivo .env

```bash
# Copie o template
copy .env.example .env

# Edite o arquivo .env com seus dados:
TELEGRAM_API_ID=seu_api_id_aqui
TELEGRAM_API_HASH=seu_api_hash_aqui
TELEGRAM_BOT_TOKEN=seu_bot_token_aqui
```


### Passo 6: Configure os Grupos e Palavras-chave

Edite o arquivo `keywords.txt` para definir quais grupos monitorar:
```txt
# Formato: [NOME_DO_GRUPO] seguido das palavras-chave
# Apenas grupos listados aqui serão monitorados

[Ofertas Tech]
ssd
monitor 34"
placa de video
notebook gamer

[Promoções Gerais]
desconto
oferta
liquidação
promoção

# [Grupo Desabilitado]
# smartphone
```

> **📌 IMPORTANTE:** O sistema monitora apenas grupos específicos. Se um grupo não estiver listado no arquivo, suas mensagens serão ignoradas.

### Passo 7: Teste e Execute

```bash
# Teste se tudo está funcionando
python test_notification.py

# Inicie o monitor (deixe rodando)
python monitor.py
```


### Estrutura do Projeto

```
ofertas-adrenaline/
├── 📄 config.py              # Gerenciamento de configurações
├── 🔍 monitor.py             # Aplicação principal (execute este)
├── ⚙️ setup_group.py         # Script de configuração automática
├── 🧪 test_notification.py   # Teste do sistema de notificações
├── 🛠️ utils.py               # Funções utilitárias
├── 📝 keywords.txt           # Suas palavras-chave (PERSONALIZE!)
├── 📋 requirements.txt       # Dependências Python
├── 🐳 Dockerfile             # Container Docker
├── 🐳 docker-compose.yml     # Orquestração Docker
├── 📄 .env.example           # Template de configuração
└── 📁 session_data/          # Dados de sessão (gerado automaticamente)
```

## 🔧 Comandos Disponíveis

### Scripts de Configuração
```bash
python setup_group.py      # Configura grupo e bot automaticamente
python test_notification.py # Testa se notificações funcionam
```

### Execução Principal  
```bash
python monitor.py          # Inicia o monitoramento (principal)
```

## 🐳 Deploy com Docker

### Método 1: Docker Compose (Recomendado)
```bash
# Configure o .env primeiro (passos acima)
docker-compose run --rm telegram-watcher
```

### Método 2: Docker Manual
```bash
# Build da imagem
docker build -t telegram-monitor .

# Execute com volume para persistir sessão
docker run -it --env-file .env \
  -v $(pwd)/session_data:/app/session_data \
  telegram-monitor
```

### Comandos de Diagnóstico
```bash
# Teste básico de configuração
python -c "from config import MonitorConfig; print('✅ OK')"

# Teste completo do sistema
python test_notification.py

# Verificação detalhada (manual)
python -c "
from config import MonitorConfig
config = MonitorConfig()
print(f'API ID: {bool(config.api_id)}')
print(f'API Hash: {bool(config.api_hash)}')
print(f'Bot Token: {bool(config.bot_token)}')
print(f'Chat ID: {bool(config.notification_chat_id)}')
"
```


### Adicionando Grupos e Palavras-chave
```txt
# keywords.txt - Exemplo avançado

[Tech Deals Brasil]
rtx 4060
ssd nvme
monitor 144hz

[Grupo Ofertas SP]
desconto.*%        # Regex: "desconto" seguido de porcentagem
oferta|promoção    # Qualquer uma das duas palavras

[Hardware Extreme]
placa mãe
processador amd
memória ram

# [Grupo Pausado]
# smartphone
# # Este grupo não será monitorado
```

### Modificando Comportamento
- **Arquivo:** `utils.py` → função `check_keywords_in_message()`
- **Personalização:** Adicione lógica para regex, case-sensitive, etc.
- **Arquivo:** `monitor.py` → ajustar lógica de correspondência de grupos

## 🚀 Vantagens deste Sistema

- **✅ Gratuito:** Usa API oficial do Telegram
- **✅ Tempo Real:** Notificações instantâneas  
- **✅ Confiável:** Funciona 24/7 sem interrupções
- **✅ Simples:** Scripts automatizados para tudo
- **✅ Flexível:** Personalize palavras-chave facilmente
- **✅ Seguro:** Credenciais em arquivo `.env` local

## 📄 Dependências

- **telethon:** Cliente oficial do Telegram para Python
- **python-dotenv:** Gerenciamento seguro de variáveis de ambiente

## ⚖️ Licença e Uso

Este projeto é para uso educacional e pessoal. Respeite os [Termos de Serviço do Telegram](https://telegram.org/tos).

---

> 💡 **Dica:** Para uso profissional, considere rodar em uma VPS com Docker para monitoramento 24/7!
