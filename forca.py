import random


def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvedor", "inteligencia", "computador", "teclado", "software"]
    return random.choice(palavras)


def exibir_forca(tentativas):
    estagios = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        ''',
        '''
           ------
           |    |
           |
           |
           |
           |
        '''
    ]
    return estagios[tentativas]


def jogar():
    palavra = escolher_palavra()
    letras_descobertas = ["_" for _ in palavra]
    tentativas = 6
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Digite 'sair' a qualquer momento para encerrar o jogo.\n")

    while tentativas >= 0:
        print(exibir_forca(tentativas))
        print("Palavra:", " ".join(letras_descobertas))
        print("Letras tentadas:", ", ".join(letras_tentadas))

        entrada = input("Digite uma letra (sair para sair): ").lower()

        if entrada == "sair":
            print("Você saiu do jogo.")
            break

        if len(entrada) != 1 or not entrada.isalpha():
            print("Digite apenas uma letra.")
            continue

        if entrada in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(entrada)

        if entrada in palavra:
            for i in range(len(palavra)):
                if palavra[i] == entrada:
                    letras_descobertas[i] = entrada
            if "_" not in letras_descobertas:
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            tentativas -= 1
            if tentativas < 0:
                print(exibir_forca(0))
                print("Você perdeu! A palavra era:", palavra)
                break

if __name__ == "__main__":
    jogar()
