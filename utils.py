
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
