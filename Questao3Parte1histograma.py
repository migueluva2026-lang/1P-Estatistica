import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

dados = [5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10,
         11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 14, 14, 14, 14, 14, 14,
         15, 15, 16, 19, 22]

# Definindo intervalos de largura 3
intervalos_dados = ['4-6', '7-9', '10-12', '13-15', '16-18', '19-21', '22-24']

# Conta frequências por intervalo
frequencias_dados = []
for intervalo in intervalos_dados:
    inicio, fim = map(int, intervalo.split('-'))
    count = sum(1 for x in dados if inicio <= x <= fim)
    frequencias_dados.append(count)

# Calcula pontos médios
pontos_medios_dados = [(int(i.split('-')[0]) + int(i.split('-')[1])) / 2 for i in intervalos_dados]

# Cria o histograma com intervalos de 3
plt.figure(figsize=(12, 6))
plt.bar(pontos_medios_dados, frequencias_dados, color='skyblue', width=2.5, edgecolor='black') # Largura ajustada
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.xticks(pontos_medios_dados, intervalos_dados)

for i, freq in enumerate(frequencias_dados):
    plt.text(pontos_medios_dados[i], freq + 0.5, str(freq), ha='center', va='bottom')

plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()