import random
def escolha(sala):
    caminho = 1 , 2
    print()
    print("Você esta na sala ",sala)
    print("[1] - Caminho Vermelho")
    print("[2] - Caminho Preto")
    escolha = int(input("Escolha o seu caminho "))
    print()
    escolha -= 1
    while escolha < 0 or escolha > 1:
        print()
        print("Este caminho não existe. Digite 1 ou 2")
        print()
        print("[1] - Caminho Vermelho")
        print("[2] - Caminho Preto")
        escolha = int(input("Escolha o seu caminho "))
        print()
        escolha -= 1
    return sala + caminho[escolha]
def sala6(sala):
    print()
    print("Você esta na sala ",sala)
    print("[2] - Caminho Preto")
    print()
    escolha = int(input("Escolha o seu caminho "))
    print()
    escolha -= 1
    sala = 8
    return sala
def sala8(sala):
    print()
    print("Você esta na sala ",sala)
    print("[1] - Caminho Vermelho")
    print("[2] - Caminho Preto")
    escolha = int(input("Escolha o seu caminho "))
    print()
    while (escolha == 1):
          print()
          print("Parabéns, você saiu do laboratório!")
          print()
          input("Digite ENTER para finalizar")
    while (escolha == 2):
          sala = random.randint(1,5)
          print()
          print("Oh não! Você encontrou um portal e foi teletransportado para a sala", sala)
          print()
          input("Digite ENTER para continuar")
          return sala
def sala9(contador):
    if contador > 6:
         print()
         print("Você chegou a Sala 9, porém estourou o limite de tentativas. Tente outra vez!")
         print()
         input("Digite ENTER para finalizar")
    else:
         print()
         print("Parabéns, você saiu do labirinto!")
         print()
         input("Digite ENTER para finalizar")

def main():
    sala = 1
    contador = 0
    while sala != 9 and contador < 10:
        contador += 1
        if sala != 6 and sala != 8:
            sala = escolha(sala)
        elif sala == 6:
            sala = sala6(sala)
        else:
            sala = sala8(sala) 
    sala9 (contador)
if __name__ == "__main__":
    main()
