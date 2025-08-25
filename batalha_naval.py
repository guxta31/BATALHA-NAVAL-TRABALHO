# batalha_naval.py

# Inicializa o tabuleiro 10x10 com zeros
tabuleiro = [[0 for _ in range(10)] for _ in range(10)]

# Função para posicionar navio horizontal
def posicionar_horizontal(x, y, tamanho):
    for i in range(tamanho):
        tabuleiro[y][x + i] = 3

# Função para posicionar navio vertical
def posicionar_vertical(x, y, tamanho):
    for i in range(tamanho):
        tabuleiro[y + i][x] = 3

# Função para posicionar navio diagonal (↘)
def posicionar_diagonal_direita(x, y, tamanho):
    for i in range(tamanho):
        tabuleiro[y + i][x + i] = 3

# Função para posicionar navio diagonal (↙)
def posicionar_diagonal_esquerda(x, y, tamanho):
    for i in range(tamanho):
        tabuleiro[y + i][x - i] = 3

# Posiciona os quatro navios
posicionar_horizontal(6, 7, 4)         # Navio horizontal
posicionar_vertical(5, 3, 3)           # Navio vertical
posicionar_diagonal_direita(0, 0, 3)   # Navio diagonal ↘
posicionar_diagonal_esquerda(6, 0, 3)  # Navio diagonal ↙

# Exibe o tabuleiro completo
print("Tabuleiro Batalha Naval (0 = vazio, 1 = navio):\n")
for linha in tabuleiro:
    print(" ".join(str(celula) for celula in linha))
