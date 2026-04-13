print('-----Bem-vindo ao jogo de par ou ímpar!-----')
escolha1 = input('Jogador 1, escolha par ou ímpar: ')
if escolha1=="par":
    escolha2 = "ímpar"
else:    escolha2 = "par"
print(f'Jogador 1 escolheu {escolha1} e Jogador 2 escolheu {escolha2}.')
jogador1 = int(input('informe um número: '))
jogador2 = int(input('informe outro número: '))

numero = jogador1 + jogador2

if numero %2 != 0:
    print('ímpar ganhou!')
else:    print('par ganhou!')