contador = 1
#enquanto o contador for <6, o programa deve perguntar pro usuário se ele quer adicionar um valor no contador ou não
while contador < 6:
    resposta = input("Deseja adicionar um valor no contador? (s/n) ")
    if resposta.lower() == 's':
        contador += 1
        print(f"Contador atualizado: {contador}")
    elif resposta.lower() == 'n':
        print("Contador não atualizado.")
    else:
        print("Resposta inválida. Por favor, responda com 's' ou 'n'.")



