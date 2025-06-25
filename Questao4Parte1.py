import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

arquivo = 'Dados_EB_py.xlsx'

try:
    df = pd.read_excel(arquivo, skiprows=1)
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não está na mesma pasta que o código.")
    exit()

df['Anos'] = pd.to_numeric(df['Anos'], errors='coerce')
df = df.dropna(subset=['Anos'])

# Definindo intervalos de 5 anos 
bins = [19, 24.999, 29.999, 34.999, 39.999, 44.999, 49.999]
labels = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49']

# Cria uma nova coluna de Faixa Etária
df['Faixa_Etaria'] = pd.cut(df['Anos'], bins=bins, labels=labels, right=True,)

# Conta a quantidade de funcionários em cada faixa
contagem = df['Faixa_Etaria'].value_counts().sort_index()

# Faz o gráfico em sí
plt.figure(figsize=(10, 6))
bars = plt.bar(contagem.index, contagem.values, color='lightskyblue', edgecolor='black', alpha=0.7)

plt.xlabel('Idade (Anos)')
plt.ylabel('Frequência')
plt.title('Idade dos Funcionários')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Quantidade exatada da frequencia em cima das barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()