# Não pode usar mais de um bloco de If e Else
# 1 = Caminho Vermelho / 2 = Caminho Preto

interacoes = 0
LIMITE_INTERACOES = 7

while (interacoes <= LIMITE_INTERACOES):
     print("Você está no caminho 1")
     print("[1] - Caminho Vermelho")
     print("[2] - Caminho Preto")
     escolha = int(input("Escolha seu caminho: "))
     while (escolha == 1):
          print("Você está no caminho 2")
          print("[1] - Caminho Vermelho")
          print("[2] - Caminho Preto")
          escolha = int(input("Escolha seu caminho: "))
          interacoes = interacoes + 1
          while (escolha == 1):
               print("Você está no caminho 3")
               print("[1] - Caminho Vermelho")
               print("[2] - Caminho Preto")
               escolha = int(input("Escolha seu caminho: "))
               interacoes = interacoes + 1
               while (escolha == 1):
                    print("Você está no caminho 4")
                    print("[1] - Caminho Vermelho")
                    print("[2] - Caminho Preto")
                    escolha = int(input("Escolha seu caminho: "))
                    interacoes = interacoes + 1
                    while (escolha == 1):
                         print("Você está no caminho 5")
                         print("[1] - Caminho Vermelho")
                         print("[2] - Caminho Preto")
                         escolha = int(input("Escolha seu caminho: "))
                         interacoes = interacoes + 1
                         while (escolha == 1):
                              print("Você está no caminho 6")
                              print("[2] - Caminho Preto")
                              escolha = int(input("Escolha seu caminho: "))
                              interacoes = interacoes + 1
                              while (escolha == 2):
                                   print("Você está no caminho 8")
                                   print("[1] - Caminho Vermelho")
                                   print("[2] - Caminho Preto")
                                   escolha = int(input("Escolha seu caminho: "))
                                   interacoes = interacoes + 1
                                   while (escolha == 1):
                                        print("Parabéns, você chegou ao seu destino!")
                                        
     while (escolha == 2):
          print("Você está no caminho 3")
          escolha = int(input("Escolha 1 para a direita ou 2 para a esquerda: "))

     interacoes = interacoes + 1