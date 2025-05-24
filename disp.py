def logica():
    print("-" * 59)
    print('-' * 19 + "Lógica de Programação" + '-' * 19)
    print("-" * 59)
    print("Lógica de Programação - PSG\nhttps://www.ead.senac.br/gratuito/logica-de-programacao-psg/")
    print("Lógica de Programação e Linguagem Java\nhttps://unieducar.org.br/catalogo/curso/logica-de-programacao-e-linguagem-java")
    print("Curso de Lógica de Programação\nhttps://www.udemy.com/course/curso-gratuito-de-logica-de-programacao/?srsltid=AfmBOopy816luGFj7z500IUl7jxgi0xBuVXNm-95oTQw37gkzH_fs2Vs")
    print("Lógica de Programação\nhttps://betrybe.com/cursos/logica-de-programacao")
    print("Lógica de programação para iniciantes\nhttps://www.learncafe.com/cursos/logica-de-programacao-iniciantes")

    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")

def web():
    print("-" * 59)
    print('-' * 20 + "Html/css/JavaScript" + '-' * 20)
    print("-" * 59)
    print("Curso completo de HTML, CSS e Javascript\nhttps://cursa.app/pt/ebook-gratuito/curso-completo-de-html-css-e-javascript-para-se-tornar-um-desenvolvedor-front-end")
    print("Programação WEB - HTML 5, CSS 3 e JavaScript\nhttps://www.learncafe.com/cursos/programacao-web---html-5%2C-css-3-e-javascript")
    print("Programação WEB\nhttps://sujeitoprogramador.com/minicurso/")
    print("Curso de programação - JavaScript do Zero\nhttps://www.betrybe.com/curso-de-programacao-javascript-do-zero")
    print("Curso de HTML, CSS e JavaScript completo com certificado\nhttps://horadecodar.com.br/curso-de-html-css-e-javascript/")

    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")

def python():
    print("-" * 59)
    print('-' * 22 + "Cursos de Python" + '-' * 21)
    print("-" * 59)
    print("Curso Rápido de Python 3\nhttps://www.udemy.com/course/curso-rapido-de-python/")
    print("Curso de Programação em Python Online\nhttps://www.primecursos.com.br/programacao-em-python/")
    print("Curso Online Grátis Python\nhttps://www.realizzarecursos.com.br/cursos/curso-de-python/")
    print("Linguagem de Programação Python - Básico\nhttps://www.ev.org.br/cursos/linguagem-de-programacao-python-basico")
    print("Curso online Python – Programação e Desenvolvimento\nhttps://unieducar.org.br/catalogo/curso/python-programacao-e-desenvolvimento-de-solucoes")

    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")

def cyber():
    print("-" * 59)
    print('-' * 23 + "CyberSegurança" + '-' * 22)
    print("-" * 59)
    print("Introduction to Cybersecurity\nhttps://www.netacad.com/pt/courses/introduction-to-cybersecurity?courseLang=en-US")
    print("Data and Cybersecurity - Coursera\nhttps://app.santanderopenacademy.com/pt-BR/program/coursera-data-and-cybersecurity")
    print("Segurança Cibernética: Controles 1 a 6 do CIS Controls\nhttps://www.escolavirtual.gov.br/curso/1073")
    print("Cybersecurity\nhttps://www.eucapacito.com.br/cursos/cybersecurity/")
    print("Código Seguro I (A1 a A5)\nhttps://www.udemy.com/course/wp-codigo-seguro-1/")

    while True:
        voltar = input("\nDeseja voltar? (S/N) ").strip().lower()
        if voltar in ["s", "sim"]:
            return  # volta para a função anterior sem fazer nada
        else:
            print("Esta resposta não é válida! Digite 'S' ou 'Sim'.")




def cursodisponivel():
    while True:
        print("-" * 59)
        print('-' * 21 + "Cursos Disponveis" + '-' * 21)
        print("-" * 59)
        print('1 - Lógica de Programação')
        print('2 - Html/css/JavaScript')
        print('3 - Python')
        print('4 - CyberSegurança')
        print('5 - Voltar')
        print("=" * 40)
        escolha = input('Digite o número de opção: ')

        if escolha == '1':
            logica()

        elif escolha == '2':
            web()

        elif escolha == '3':
            python()

        elif escolha == '4':
            cyber()

        elif escolha == '5':
            break
        else:
            print('Opção inválida, tente novamente. ')

if __name__ == "__main__":
    cursodisponivel()
