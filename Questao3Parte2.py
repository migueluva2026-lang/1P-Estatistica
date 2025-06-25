import matplotlib.pyplot as plt

#dados não importados, preferencia pra não ter que ficar importando o arquivo e dar erro quando executar
# Fique salvo que eu importei nos 2 primeiros códigos das duas primeiras questões, então caso eu precisasse eu poderia ter feito, só foi preferencia 
dados = [2, 2, 3, 10, 13, 13, 14, 15, 15, 16, 16, 18, 18, 20, 21, 22, 22, 23, 24, 25, 25, 26, 27, 29, 29, 30, 32, 36, 42, 44, 45, 45, 46, 48, 52, 58, 59, 61, 61, 61, 65, 66, 66, 68, 75, 78, 80, 89, 90, 92, 97]

# Definindo o número de intervalos desejado
num_intervalos = 5

# Criando o histograma
plt.figure(figsize=(10, 6))
plt.hist(dados, bins=num_intervalos, edgecolor='black', color='lightcoral')

# Adicionando rótulos e título
plt.xlabel('Número de Casas por Quarteirão')
plt.ylabel('Frequência (Número de Quarteirões)')
plt.title('Histograma do Número de Casas por Quarteirão')

# Adicionando linhas de grade horizontais (opcional)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()