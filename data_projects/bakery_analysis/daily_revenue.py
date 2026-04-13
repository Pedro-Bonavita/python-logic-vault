import matplotlib.pyplot as plt

# Dados consolidados do arquivo 
datas = ['01/01', '02/01', '03/01', '04/01']
faturamento = [1355.00, 1347.50, 1340.00, 1595.00]

plt.figure(figsize=(10, 6))
plt.plot(datas, faturamento, marker='o', color='#B8860B', linewidth=2, markersize=8)

# Adicionando rótulos de dados
for i, valor in enumerate(faturamento):
    plt.text(datas[i], valor + 15, f'R$ {valor:,.2f}', ha='center', fontweight='bold')

plt.title('Evolução do Faturamento Diário - Padaria Pão de Ouro', fontsize=14)
plt.ylabel('Faturamento (R$)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(1300, 1700) 
plt.show()