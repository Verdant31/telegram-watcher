# Telegram Deal Monitor

Um aplicativo Python que monitora mensagens do Telegram em busca de palavras-chave específicas e envia notificações via Telegram quando ofertas promocionais são detectadas.

## Recursos

- Monitoramento de mensagens do Telegram em tempo real
- Detecção de ofertas baseada em palavras-chave
- Notificações via bot do Telegram (para receber alertas reais)
- Lista de palavras-chave personalizável
- Configuração segura de variáveis de ambiente
- Suporte ao Docker para deploy fácil
- Configuração automática de grupo de notificações

## ⚠️ IMPORTANTE: Por que usar um bot?

**Problema:** Quando você mesmo envia mensagens no Telegram, o app não gera notificações push.
**Solução:** Usar um bot para enviar as notificações garante que você receba alertas reais no telefone/desktop.

## Início Rápido

### 1. Clone o repositório:
```bash
git clone <repository-url>
cd telegram-watch
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais do Telegram:
- Visite https://my.telegram.org
- Faça login com seu número de telefone
- Vá para "API development tools"
- Crie uma nova aplicação
- Anote o `api_id` e `api_hash`

### 4. 🤖 Configure um bot do Telegram (RECOMENDADO):

Execute o script de configuração do bot:
```bash
python setup_bot.py
```

O script irá te guiar através do processo:

#### 4.1. Criando o bot no Telegram:
1. Abra o Telegram e procure por **@BotFather**
2. Envie o comando: `/newbot`
3. Escolha um nome para seu bot (ex: "Monitor de Ofertas")
4. Escolha um username para seu bot (deve terminar com 'bot', ex: "ofertas_monitor_bot")
5. **Copie o TOKEN** que o BotFather enviar
6. Cole o token no script quando solicitado

#### 4.2. O que o script faz:
- ✅ Valida o token do bot
- ✅ Salva o token no arquivo `.env`
- ✅ Mostra os próximos passos

### 5. Configure o arquivo .env:
- Copie `.env.example` para `.env` ou deixe o script criar automaticamente
- Preencha suas credenciais reais:
```bash
TELEGRAM_API_ID=seu_api_id_aqui
TELEGRAM_API_HASH=seu_api_hash_aqui
TELEGRAM_BOT_TOKEN=seu_bot_token_aqui  # Configurado pelo setup_bot.py
TELEGRAM_SESSION=session_data/monitor
TELEGRAM_NOTIFICATION_CHAT_ID=  # Será preenchido automaticamente
```

### 6. Configure o grupo de notificações automaticamente:
```bash
python setup_group.py
```
**Este script irá:**
- Conectar ao Telegram
- Criar automaticamente um grupo chamado "Notificações de Ofertas"
- Atualizar o arquivo .env com o ID do grupo
- Enviar uma mensagem de confirmação no grupo criado

### 7. 🔗 Adicione o bot ao grupo:
**IMPORTANTE:** Após executar o `setup_group.py`, você precisa:
1. Abrir o grupo "Notificações de Ofertas" no Telegram
2. Tocar em "Adicionar membros"
3. Procurar pelo username do seu bot
4. Adicionar o bot ao grupo

💡 **Isso é necessário para que o bot possa enviar notificações e você receba alertas reais!**
- Lista de palavras-chave personalizável
- Configuração segura de variáveis de ambiente
- Suporte ao Docker para deploy fácil
- Configuração automática de grupo de notificações

## Início Rápido

### 1. Clone o repositório:
```bash
git clone <repository-url>
cd telegram-watch
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais do Telegram:
- Visite https://my.telegram.org
- Faça login com seu número de telefone
- Vá para "API development tools"
- Crie uma nova aplicação
- Anote o `api_id` e `api_hash`

### 4. Crie um bot do Telegram (para enviar notificações):
- Abra o Telegram e procure por @BotFather
- Envie `/newbot` para criar um novo bot
- Escolha um nome e username para seu bot
- Anote o **token do bot** que será fornecido
- Este bot enviará as notificações, garantindo que você receba alertas

### 5. Configure o arquivo .env:
- Copie `.env.example` para `.env` ou crie um novo arquivo `.env`
- Preencha suas credenciais reais:
```bash
TELEGRAM_API_ID=seu_api_id_aqui
TELEGRAM_API_HASH=seu_api_hash_aqui
TELEGRAM_BOT_TOKEN=seu_bot_token_aqui
TELEGRAM_SESSION=session_data/monitor
TELEGRAM_NOTIFICATION_CHAT_ID=
```

### 6. Configure o grupo de notificações automaticamente:
```bash
python setup_group.py
```
**Este script irá:**
- Conectar ao Telegram
- Criar automaticamente um grupo chamado "Notificacoes de Ofertas"
- Atualizar o arquivo .env com o ID do grupo
- Enviar uma mensagem de confirmação no grupo criado

**IMPORTANTE:** Após executar este script, você precisa adicionar manualmente seu bot ao grupo:
1. No Telegram, procure pelo grupo "Notificacoes de Ofertas" que foi criado
2. Entre no grupo e clique em "Adicionar membros"
3. Procure pelo seu bot (use o nome que você deu ao criar com @BotFather)
4. Adicione o bot ao grupo
5. Isso é necessário para que o bot possa enviar notificações e você receba alertas reais

### 8. Configure as palavras-chave em `keywords.txt`

### 9. Teste o sistema:
```bash
python test_notification.py
```
Este comando enviará uma mensagem de teste para verificar se tudo está funcionando.

### 10. Execute o monitor:
```bash
python monitor.py
```

## Configuração

### Variáveis de Ambiente Obrigatórias

Crie um arquivo `.env` com as seguintes variáveis:

- `TELEGRAM_API_ID`: ID da API do Telegram (obtenha em https://my.telegram.org)
- `TELEGRAM_API_HASH`: Hash da API do Telegram
- `TELEGRAM_BOT_TOKEN`: Token do bot (obtenha criando um bot com @BotFather)
- `TELEGRAM_SESSION`: Caminho do arquivo de sessão (padrão: session_data/monitor)
- `TELEGRAM_NOTIFICATION_CHAT_ID`: ID do grupo de notificações (configurado automaticamente pelo setup_group.py)

### 🤖 Como Criar um Bot do Telegram (Passo a Passo Detalhado)

#### Método 1: Usar o script automatizado
```bash
python setup_bot.py
```

#### Método 2: Manual
1. **Abra o Telegram** em qualquer dispositivo
2. **Procure por @BotFather** (é o bot oficial do Telegram para criar bots)
3. **Inicie uma conversa** com @BotFather
4. **Envie o comando** `/newbot`
5. **Escolha um nome** para seu bot (ex: "Monitor de Ofertas Adrenaline")
6. **Escolha um username** (deve terminar com "bot", ex: "ofertas_adrenaline_bot")
7. **Copie o token** que aparecerá na mensagem (formato: `123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`)
8. **Adicione o token** no arquivo `.env` na linha `TELEGRAM_BOT_TOKEN=`

#### ⚠️ Dicas importantes sobre o bot:
- **Guarde o token com segurança** - ele dá controle total sobre seu bot
- **Não compartilhe o token** com ninguém
- **O username deve ser único** - se estiver em uso, tente outro
- **Você pode editar nome e foto** do bot depois no @BotFather

### Configuração de Palavras-chave

Edite o arquivo `keywords.txt` para especificar quais palavras-chave monitorar:

```txt
# Palavras-chave para monitoramento de ofertas
# Uma palavra-chave por linha
# Linhas começando com # são comentários

ssd
placa de video
notebook
promoção
desconto
oferta
liquidação
```

## Como Obter Credenciais da API do Telegram

1. Visite https://my.telegram.org
2. Faça login com seu número de telefone
3. Vá para "API development tools"
4. Crie uma nova aplicação
5. Anote o `api_id` e `api_hash`

## Estrutura do Projeto

```
telegram-watch/
├── config.py              # Configuração e setup de ambiente
├── monitor.py             # Aplicação principal de monitoramento
├── setup_group.py         # Script para configurar grupo automaticamente
├── get_chat_id.py         # Script alternativo para obter Chat ID
├── test_notification.py   # Script de teste para verificar notificações
├── check_config.py        # Script para verificar configuração
├── utils.py               # Funções utilitárias para processamento de palavras-chave
├── keywords.txt           # Palavras-chave para monitorar
├── requirements.txt       # Dependências Python
├── Dockerfile             # Configuração do container Docker
├── docker-compose.yml     # Setup do Docker Compose
├── .env.example           # Template de variáveis de ambiente
└── session_data/          # Armazenamento de sessão do Telegram
```

## Como Funciona

1. A aplicação conecta ao Telegram usando a biblioteca Telethon
2. Monitora mensagens recebidas em tempo real
3. Cada mensagem é verificada contra as palavras-chave em `keywords.txt`
4. Quando uma correspondência é encontrada, uma notificação do Telegram é enviada para o grupo configurado
5. A notificação inclui as palavras-chave encontradas e a mensagem original

## Comandos Disponíveis

### Configuração inicial
- `python setup_bot.py` - Configura o bot do Telegram (recomendado)
- `python setup_group.py` - Cria o grupo de notificações automaticamente

### Testando o sistema
- `python test_notification.py` - Envia uma mensagem de teste para verificar se tudo funciona

### Executando o monitor
- `python monitor.py` - Inicia o monitoramento de mensagens

## Como Funciona

1. A aplicação conecta ao Telegram usando a biblioteca Telethon
2. Monitora mensagens recebidas em tempo real
3. Cada mensagem é verificada contra as palavras-chave em `keywords.txt`
4. Quando uma correspondência é encontrada:
   - Se o bot estiver configurado: 🤖 **Bot envia a notificação** (você recebe alerta real)
   - Se o bot não estiver configurado: 😴 Seu usuário envia (sem alerta real)
5. A notificação inclui as palavras-chave encontradas e a mensagem original

## Solução de Problemas

### Problemas Comuns

1. **"❌ Bot token não configurado"**
   - Execute `python setup_bot.py` para configurar o bot
   - Isso garantirá que você receba notificações reais

2. **"❌ Chat ID não configurado"**
   - Execute `python setup_group.py` para criar o grupo automaticamente
   - O script criará um grupo chamado "Notificações de Ofertas"

3. **"❌ Variáveis de ambiente não encontradas"**
   - Verifique se o arquivo `.env` existe na raiz do projeto
   - Confirme se `TELEGRAM_API_ID` e `TELEGRAM_API_HASH` estão preenchidos
   - Execute `python setup_bot.py` se `TELEGRAM_BOT_TOKEN` estiver vazio

4. **"❌ Erro de conexão com Telegram"**
   - Verifique suas credenciais da API em https://my.telegram.org
   - Certifique-se de que não há firewall bloqueando a conexão

5. **"❌ Notificações não chegam no telefone"**
   - **Causa mais comum:** Bot não configurado ou não adicionado ao grupo
   - **Solução:** Execute `python setup_bot.py` e adicione o bot ao grupo
   - Execute `python test_notification.py` para testar

6. **"❌ Bot não consegue enviar mensagens"**
   - Verifique se o bot foi adicionado ao grupo "Notificações de Ofertas"
   - O bot precisa estar no grupo para conseguir enviar mensagens

7. **"❌ Token do bot inválido"**
   - Verifique se o token foi copiado corretamente do @BotFather
   - O token deve ter o formato: `123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`
   - Execute `python setup_bot.py` novamente para reconfigurar

### Testando a configuração

Execute os comandos na seguinte ordem para verificar se tudo está funcionando:

```bash
# 1. Teste a configuração básica
python -c "from config import MonitorConfig; print('✅ Configuração carregada com sucesso!')"

# 2. Teste o bot (se configurado)
python setup_bot.py

# 3. Teste o grupo
python setup_group.py

# 4. Teste as notificações
python test_notification.py

# 5. Se tudo estiver funcionando, inicie o monitor
python monitor.py
```

## Deploy com Docker

Para deploy com Docker:

1. Configure as variáveis de ambiente no arquivo `.env` (veja seção de configuração acima)

2. Execute com Docker Compose:
```bash
docker-compose run --rm telegram-watcher
```

**Nota de Segurança**: O `docker-compose.yml` usa `env_file: .env` para carregar variáveis de ambiente de forma segura. Nunca coloque credenciais diretamente no docker-compose.yml!

## Estrutura do Projeto

```
telegram-watch/
├── config.py              # Configuração e setup de ambiente
├── monitor.py             # Aplicação principal de monitoramento
├── setup_bot.py           # Script para configurar bot automaticamente
├── setup_group.py         # Script para configurar grupo automaticamente
├── test_notification.py   # Script de teste para verificar notificações
├── utils.py               # Funções utilitárias para processamento
├── keywords.txt           # Palavras-chave para monitorar
├── requirements.txt       # Dependências Python
├── Dockerfile             # Configuração do container Docker
├── docker-compose.yml     # Setup do Docker Compose
├── .env.example           # Template de variáveis de ambiente
└── session_data/          # Armazenamento de sessão do Telegram
```

## Dependências

- `telethon`: Biblioteca cliente do Telegram
- `python-dotenv`: Gerenciamento de variáveis de ambiente

## 🚀 Vantagens desta Versão

- **Notificações reais**: Com bot configurado, você recebe alertas no telefone
- **Gratuito**: Sem custos - usa Telegram para notificações
- **Simples**: Scripts automatizados para configuração
- **Confiável**: API direta do Telegram sem dependências externas
- **Tempo real**: Notificações instantâneas
- **Fácil teste**: Scripts dedicados para verificar funcionalidade
- **Configuração automática**: Scripts para configurar tudo automaticamente
- **Fallback inteligente**: Se o bot falhar, usa o usuário como backup

## Licença

Este projeto é para uso educacional e pessoal. Por favor, respeite os termos de serviço do Telegram.
