import random
numero_maquina = random.randint(0,10)
deseja_adivinhar = int(input(""" Olá, vamos brincar de adivinhar numeros? Digite:
            1-Sim
            2-Não \n"""))
if deseja_adivinhar == 1: 
    while True:
   
        numero_usuario = int(input("Digite um numero de 0 até 10: "))
        
        if numero_maquina == numero_usuario :
            print(f"Parabens, voce acertou o numero escolhido que foi o {numero_maquina}")
        elif numero_usuario < 0  :
             print("voce precisa escolher um numero entre 0 e 10")
        elif numero_usuario >10:
              print("voce precisa escolher um numero entre 0 e 10")
        else:
               print(f"Infelizmente, o numero correto era {numero_maquina}")
          
        continuar = int(input("""Deseja brincar novamente?
                          3 - Sim
                          4 - Não \n"""))     

        if continuar == 3:
               numero_maquina = random.randint(0,10)
        elif continuar== 4:
               print("Ok, podemos brincar novamente quando desejar. È só me chamar novamente !")
               break
elif deseja_adivinhar == 2 :
    print("Ok, podemos brincar quando desejar. é só me chamar novamente.")
       

else:
    print("opção invalida, veja novamente as orientações.")