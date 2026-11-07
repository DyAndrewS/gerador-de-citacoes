import random

CITACOES = {
    "tecnologia": [
        "A simplicidade é a alma da eficiência. – Austin Freeman",
        "Primeiro, resolva o problema. Depois, escreva o código. – John Johnson",
        "Código limpo sempre parece que foi escrito por alguém que se importa. – Martin Fowler"
    ],
    "motivacao": [
        "O insucesso é apenas uma oportunidade para recomeçar com mais inteligência. – Henry Ford",
        "Faça o que puder, com o que tiver, onde estiver. – Theodore Roosevelt",
        "A persistência é o caminho do êxito. – Charles Chaplin"
    ],
    "filosofia": [
        "Conhece-te a ti mesmo. – Sócrates",
        "A vida não examinada não vale a pena ser vivida. – Sócrates",
        "Penso, logo existo. – René Descartes"
    ]
}

def obter_citacao_aleatoria(categoria=None):
    if categoria:
        cat_lower = categoria.lower()
        if cat_lower in CITACOES:
            return random.choice(CITACOES[cat_lower])
        else:
            raise ValueError(f"Categoria '{categoria}' não encontrada. Opções: {list(CITACOES.keys())}")
    
    todas = [citacao for lista in CITACOES.values() for citacao in lista]
    return random.choice(todas)