import matplotlib.pyplot as plt

# Preferi dizer os dados ao importar do arquivo, mas eu poderia ter importado caso fossem infinitos números
valores = [8, 7, 11, 12, 6, 13, 14, 15, 16, 5, 19, 22, 9, 10]
frequencias = [6, 5, 4, 9, 4, 1, 7, 2, 1, 2, 1, 1, 2, 5]

# DEVE criar o gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.bar(valores, frequencias, color='skyblue')  # Cria as barras

# Adiciona título e outras coisas
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Distribuição de Frequência dos Dados')

# Personaliza o eixo x para mostrar todos os valores
plt.xticks(valores)

# Adicionando as frequências acima das barras pra deixar mais legivel
for i, freq in enumerate(frequencias):
    plt.text(valores[i], freq + 0.2, str(freq), ha='center', va='bottom')

# Exibe o gráfico
plt.grid(axis='y', linestyle='--') 
plt.tight_layout() 
plt.show()