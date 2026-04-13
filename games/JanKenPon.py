# JO KEN PO
#----- Configuração inicial -----
jogador1 = input('Informe o nome do jogador 1:  ')
jogador2 = input('Informe o nome do jogador 2:  ')

pontuacao1 = 0
pontuacao2 = 0

# ---- Definição de Funções ----

# definir funções
def escolher_jogada():
    print("\n" + "="*20)
    print("JANKENPON")
    print("para escolher sua jogada, digite uma das opções: Pedra // Papel // Tesoura")
    print("="*20)
    movimento1 = input(f'{jogador1} escolha sua jogada: ').lower().strip()
    movimento2 = input(f'{jogador2} escolha sua jogada: ').lower().strip()

    return movimento1, movimento2

def jogar(movimento1, movimento2):
    print(f'{jogador1} escolheu {movimento1}')
    print(f'{jogador2} escolheu {movimento2}')

    if movimento1 == movimento2:
        print('Empate!')

    # Casos onde Jogador 1 vence
    vitoria_j1 = (movimento1 == "pedra" and movimento2 == "tesoura") or \
                 (movimento1 == "papel" and movimento2 == "pedra") or \
                 (movimento1 == "tesoura" and movimento2 == "papel")
    
    # Casos onde Jogador 2 vence
    vitoria_j2 = (movimento2 == "pedra" and movimento1 == "tesoura") or \
                 (movimento2 == "papel" and movimento1 == "pedra") or \
                 (movimento2 == "tesoura" and movimento1 == "papel")
    
    if vitoria_j1:
        print(f'{jogador1} venceu a rodada!')
        return 1
    elif vitoria_j2:
       print(f"\n{jogador2} venceu a rodada!")
       return 2
    else:
       print('Jogada inválida!')
       return -1    

def regras():
    print('Pedra ganha de Tesoura')
    print('Papel ganha de Pedra')
    print('Tesoura ganha de Papel')
    input("\nPressione Enter para voltar ao menu...")

# executar o jogo

while True:
   print("\n" + "#"*20)
   print("MENU PRINCIPAL")
   print("#"*20)
   print("1 - Ver Regras")
   print("2 - Jogar")
   print("3 - Ver Placar")
   print("4 - Sair")

   opcao = input("\nEscolha uma opção: ")

   if opcao == "1":
      regras()
    elif opcao == "2":
      while True:
         m1, m2 = escolher_jogada()
         resultado = jogar(m1, m2)
         if resultado == 1:
            pontuacao1 += 1
         elif resultado == 2:
            pontuacao2 += 1
            dnv = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
            if dnv != 's':
                print("Retornando ao menu principal...")
                break
    
    elif opcao == "3":
      print(f"\nPLACAR ATUAL: \n{jogador1}: {pontuacao1} | {jogador2}: {pontuacao2}")
      input("\nPressione Enter para voltar ao menu...")
    
    elif opcao == "4":
      print("Obrigado por jogar! Até a próxima!")
      break
   
   else:
      print("\nOpção inválida. Por favor, escolha uma opção válida.")
