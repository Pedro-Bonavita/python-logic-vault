import matplotlib.pyplot as plt

# Dados calculados a partir da soma de Total_Venda 
categorias = ['Bebidas', 'Pães', 'Salgados', 'Confeitaria']
faturamento_cat = [1740.00, 1505.00, 1297.50, 1095.00]
cores = ['#FFD700', "#D46300", "#75CC53", '#DEB887']

plt.figure(figsize=(8, 8))
# Criação do gráfico de rosca (donut)
plt.pie(faturamento_cat, labels=categorias, autopct='%1.1f%%', startangle=140, 
        colors=cores, pctdistance=0.85, wedgeprops={'width': 0.4, 'edgecolor': 'w'})

plt.title('Mix de Receita por Categoria', fontsize=14, fontweight='bold')
plt.legend(title="Categorias", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()