import matplotlib.pyplot as plt

# Dados de Quantidade_Vendida agrupados por Produto 
dados_produtos = {
    'Pão Francês': 930,
    'Pão de Queijo': 230,
    'Café Expresso': 180,
    'Coxinha': 95,
    'Chocolate Quente': 40,
    'Enroladinho': 35,
    'Sonho': 30,
    'Suco de Laranja': 25,
    'Quiche': 20,
    'Bolo de Fubá': 15,
    'Bolo de Cenoura': 12,
    'Torta de Morango': 8
}

# Ordenando do maior para o menor
produtos = sorted(dados_produtos, key=dados_produtos.get, reverse=False)
quantidades = [dados_produtos[p] for p in produtos]

# Definindo cores (Destaque para Pão Francês e Pão de Queijo)
cores = ['#DAA520' if (p == 'Pão Francês' or p == 'Pão de Queijo') else '#C0C0C0' for p in produtos]

plt.figure(figsize=(12, 8))
bars = plt.barh(produtos, quantidades, color=cores)

# Rótulos de dados nas barras
for bar in bars:
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())} un', va='center', fontsize=10)

plt.title('Ranking de Produtos mais Vendidos (Unidades)', fontsize=14)
plt.xlabel('Quantidade Total Vendida')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()