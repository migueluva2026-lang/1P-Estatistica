import matplotlib.pyplot as plt

# Intervalos de classe e suas frequências
intervalos = ['30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-65', '65-70']
frequencias = [2, 10, 18, 50, 70, 30, 18, 2]

# Encontra os pontos médios para posicionar as barras
pontos_medios = [32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5, 67.5]

# Cria o histograma (usando plt.bar para representar as barras)
plt.figure(figsize=(12, 6))
plt.bar(pontos_medios, frequencias, color='skyblue', width=4.5, edgecolor='black')

# Adiciona rótulos e título
plt.xlabel('Venda Semanal (Salários Mínimos)')
plt.ylabel('Número de Vendedores')
plt.title('Distribuição das Vendas Semanais dos Vendedores')
plt.xticks(pontos_medios, intervalos) # É para usar os pontos médios para as posições e os intervalos como rótulos

# Adiciona as frequências acima das barras
for i, freq in enumerate(frequencias):
    plt.text(pontos_medios[i], freq + 2, str(freq), ha='center', va='bottom')

# Exibe o gráfico
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()