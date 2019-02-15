# -*- coding: utf-8 -*-
# !usr/bin/python3
from random import *

# Variaveis de cores
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
YELLOW = '\033[33m'
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

# Lista com as palavras em ingles
listaPort = ["I", "You", "He", "She", "We", "With", "Have", "This", "Or", "But", "Word", "World", "Hello", "What",
             "Some", "Other", "Which", "Time", "If", "Many", "Write", "Make", "See", "Look", "More", "Come", "Number",
             "No", "My", "Your", "Water", "Fire", "First", "Second", "Third", "Who", "Side", "New", "Stop", "One", "Two",
             "Now", "Any", "Work", "Get", "Where", "After", "Only", "Man", "Woman", "Year", "Good", "Our",
             "Think", "Low", "Line", "Differ", "Much", "Before", "Right", "Old", "Boy", "Girl", "Same", "Tell"]

# Lista com as palavras correspondentes em português
listaIng = ["Eu", "Voce", "Ele", "Ela", "Nos", "Com", "ter", "Este", "Ou", "Mas", "Palavra", "Mundo", "Ola", "O que",
            "Algum", "Outro", "Qual", "Tempo", "Se", "Muitos", "Escrever", "Fazer", "Ver", "Olhar", "Mais", "Vir", "Numero",
            "Nao", "Meu", "Seu", "Agua", "Fogo", "Primeiro", "Segundo", "Terceiro", "Quem", "Lado", "Novo", "Pare", "Um", "Dois",
            "Agora", "Qualquer", "Trabalho", "Ficar", "Onde", "Depois", "Somente", "Homem", "Mulher", "Ano", "Bom", "Nosso",
            "Pensar", "Baixo", "Linha", "Deferir", "Muito", "Antes", "Direito", "Velho", "Menino", "Menina", "Mesmo", "Contar"]

vidas = 3
pontos = 0

a = randint(1, 10)
print("===="*20)
print("{}Você possui três vidas, a cada erro perde 1 vida e 50 pontos.".format(YELLOW))
print("A cada acerto você ganha 100 pontos.")
print("Por favor não utilize acentuação. Boa sorte!!{}".format(RESET))

while True:
    if a % 2 == 0:
        a = randint(0, len(listaIng) - 1)

        print("===="*20)
        res = input("\n{}Qual a tradução da palavra: {} -> {}".format(BLUE, listaIng[a], RESET))

        # Testando a resposta dada pelo usuario com a resposta da lista de palavras em portugues
        if listaPort[a].upper() == res.upper():
            print("{}Parabens você acertou!!{}".format(YELLOW, RESET))
            pontos += 100

        else:
            pontos -= 50
            vidas -= 1
            print("\n{}Que pena, você errou!".format(RED))
            print("A tradução da palavra {} é {}.".format(listaIng[a], listaPort[a]))
            print("Voce ainda possui {} vidas{}\n".format(vidas, RESET))

        if vidas <= 0:
            print("\n{}Você não possui mais vidas!".format(RED))

            if pontos <= 0:
                pontos = 0
                print("Você conseguiu {} pontos{}\n\n".format(pontos, RESET))
                break
            else:
                print("Você conseguiu {} pontos{}\n\n".format(pontos, RESET))
                break

    else:
        a = randint(0, len(listaPort) - 1)

        print("===="*20)
        res = input("\n{}Qual a tradução da palavra: {} -> {}".format(BLUE, listaPort[a], RESET))

        # Testando a resposta dada pelo usuario com a resposta da lista de palavras em ingles
        if listaIng[a].upper() == res.upper():
            print("{}Parabens você acertou!!{}".format(YELLOW, RESET))
            pontos += 100

        else:
            pontos -= 50
            vidas -= 1
            print("{}Que pena, você errou!{}".format(RED, RESET))
            print("A tradução da palavra {} é {}.".format(listaPort[a], listaIng[a]))
            print("Voce ainda possui {} vidas\n".format(vidas))

        if vidas <= 0:
            print("\n{}Você não possui mais vidas!".format(RED))

            if pontos <= 0:
                pontos = 0
                print("Você conseguiu {} pontos{}\n\n".format(pontos, RESET))
                break
            else:
                print("Você conseguiu {} pontos{}\n\n".format(pontos, RESET))
                break
