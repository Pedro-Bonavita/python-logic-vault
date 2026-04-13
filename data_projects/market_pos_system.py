
lista_produtos = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Óleo",
    "Água mineral"]

lista_preco = [2.50, 5.00, 7.25, 4, 3.45]

# para criarmos uma função
# para criarmos um apanhado de códigos
# armazenar eles dentro de um bloco e dar nome

# função 1 - ver produtos
def ver_produtos():
   print (f'Os produtos disponíveis são: {lista_produtos}')
   print (f'Os preços dos produtos são: {lista_preco}')

def adicionar_produto():
    novo_produto = input('Digite o nome do produto: ')
    novo_preco = float(input('Digite o preço do produto: '))
    lista_produtos.append(novo_produto)
    # /\ CHAMAMOS A LISTA E ATRIBUIMOS A FUNÇÃO APPEND (ADICIONAR) E PASSAMOS O NOVO PRODUTO COMO ARGUMENTO
    lista_preco.append(novo_preco)
    print(f'Produto {produto} adicionado com sucesso!')

print('-----MENU DO MERCADINHO-----')
print('Escolha uma opção:')
print('1- ver produtos')
print('2- Cadastrar novo produto')
opcao = int(input('informe a opção desejada'))

# o comando if serve para condicionar algo
# if condição operador (==) resposta:
if opcao == 1:
    # o que deve executar
    ver_produtos()
elif opcao == 2:
    # o comando elif é a combinação dos termos else (se nao) if (se)
    adicionar_produto()
    ver_produtos()
else:
    print('opção não encontrada')