from login import criar_conta, fazer_login
from sobre import sobre
from Acad import acadprin
from disp import cursodisponivel

def menu():

    while True:
        print("-" * 59)
        print('-' * 23 + "Seja bem-vindo" + '-' * 22)
        print('-' * 23 + "Menu de Acesso" + '-' * 22)
        print("-" * 59)
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Sair")
        print("="*40)
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            fazer_login()
        elif escolha == "3":
            print(" Encerrando o programa... Até logo!")
            break
        else:
            print(" Opção inválida. Tente novamente.\n")

def principal():

    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Principal" + '-' * 22)
        print("-" * 59)
        print("\n1-Cursos Disponíveis             ░░╔══════════════╗░░\n2-Academia                       ░░║   Academia   ║░░\n3-Sobre                          ░░║      de      ║░░\n4-Sair                           ░░║  Aprendizado ║░░\n                                 ░░╚═════╦══╦═════╝░░")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cursodisponivel()

        elif escolha == "2":
            acadprin()

        elif escolha == "3":
            sobre()

        elif escolha == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
