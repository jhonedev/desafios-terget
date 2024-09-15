def inverterPalavra(palavra):
    palavraInvertida = ''
    for letra in range(len(palavra) - 1, -1, -1):
        palavraInvertida += palavra[letra]
    return palavraInvertida

palavraEscolhida = input("Digite uma palavra: ")
print(f'Palavra invertida: {inverterPalavra(palavraEscolhida)}')
