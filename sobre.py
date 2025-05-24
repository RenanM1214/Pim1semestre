def sobre():
    print("-" * 59)
    print('-' * 23 + "Sobre Projeto" + '-' * 22)
    print("-" * 59)
    print("\nEste projeto foi desenvolvido como parte do Trabalho Interdisciplinar (PIM)")
    print("do curso de Análise e Desenvolvimento de Sistemas da Universidade Paulista – UNIP,")
    print("campus II São José do Rio Preto. A proposta é criar uma academia de programação")
    print("voltada a ajudar pessoas que desejam aprender ou aprimorar seus conhecimentos em desenvolvimento.\n")

    print("A plataforma oferece uma experiência simples, acessível e educativa,")
    print("com foco em conteúdos e práticas voltadas à programação.")
    print("Todo o sistema foi desenvolvido utilizando a linguagem Python,")
    print("e os dados são armazenados em arquivos no formato JSON,")
    print("garantindo leveza e fácil manutenção.\n")

    print("O projeto foi idealizado e construído pelos alunos:")
    print("- Renan Mattos")
    print("- João Pedro Ferreira")
    print("- João Paulo Aquino")
    print("- Leonardo da Silva")

    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")

if __name__ == "__main__":
    sobre()
