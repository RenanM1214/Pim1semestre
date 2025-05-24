import json
from forca import jogar


def material_deapoio (): ## material de apoio
    print("-" * 59)
    print('-' * 21 + "Material de apoio" + '-' * 21)
    print("-" * 59)
    print(
        "\n Para você que tem interesse em começar na área da programação ou até mesmo aprimorar seus conhecimentos.")
    print(
        "É muito importante escolher por onde começar, assim fica mais fácil entender e não se desanimar ou desistir.")
    print("A programação pode parecer difícil, mas com persistência e paciência, tudo é possível!")
    print(
        "\n🚨 Dica: Aprender a programar não acontece da noite para o dia. Evite pressa e foque no aprendizado consistente.\n")

    print("\n🔹 Lógica de Programação")
    print("   ➤ Ponto de partida para todo programador.")
    print("   ➤ Aprenda a pensar de forma lógica e estruturada.")
    print("   ➤ Trabalhe com comandos, condições e repetições.")
    print("   ➤ É a base de qualquer linguagem de programação.")

    print("\n🔹 HTML / CSS / JavaScript")
    print("   ➤ Tecnologias fundamentais para criar sites e aplicações web.")
    print("   ➤ HTML: estrutura e organização do conteúdo.")
    print("   ➤ CSS: estilo visual — cores, tamanhos, layout.")
    print("   ➤ JavaScript: interatividade — menus, animações, formulários.")

    print("\n🔹 Python")
    print("   ➤ Linguagem excelente para iniciantes e profissionais.")
    print("   ➤ Usado em desenvolvimento de aplicações, automação, análise de dados, IA e muito mais.")
    print("   ➤ Fácil de aprender, poderosa para avançar!")

    print("\n🔹 CyberSegurança")
    print("   ➤ Área essencial com o aumento da digitalização.")
    print("   ➤ Aprenda sobre proteção de sistemas, identificação de ameaças e práticas seguras.")
    print("   ➤ Conceitos como senhas fortes, criptografia e defesa contra ataques cibernéticos.")

    print("\n💡 Comece devagar, seja curioso e mantenha a prática constante.")
    print("🚀 Bons estudos e boa sorte na sua jornada como programador!")
    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")


def acadprin():  ## função principal
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Academia" + '-' * 22)
        print("-" * 59)
        print('1 - Material de apoio')
        print('2 - Jogos para aprender')
        print('3 - Voltar')
        print("=" * 40)
        escolha= input('Digite o número de opção: ')
        if escolha == '1':
            material_deapoio()

        elif escolha == '2':
            jogar()

        elif escolha == '3':
            break
        else:
            print('Opção inválida, tente novamente. ')

if __name__ == '__main__':
    acadprin()
