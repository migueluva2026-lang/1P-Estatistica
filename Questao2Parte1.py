import pandas as pd

Arquivo = pd.read_excel('Dados_EB_py.xlsx', sheet_name='CD-Brasil', skiprows=4) #Importa arquivo no dataframe CD-Brasil
# print(df.columns) Para debug

# Criei um filtro para excluir Subtotais e Totais que estão no arquivo, já que estragariam o calculo
estados_validos = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO',
               'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA',
               'MG', 'ES', 'RJ', 'SP',
               'PR', 'SC', 'RS',
               'MS', 'MT', 'GO', 'DF']

# Limita o arquivo ao remover tudo que estiver na coluna B que não esteja no filtro de estados_validos
Arquivo = Arquivo[Arquivo['Unnamed: 1'].isin(estados_validos)]

# Cria classes de população
classesP = [0, 2000000, 5000000, 10000000, 20000000, 50000000]
classes2P = ['Até 2M', '2M-5M', '5M-10M', '10M-20M', '20M+']
Arquivo['Classe Populacao'] = pd.cut(Arquivo['População'], bins=classesP, labels=classes2P)


# Cria classes de densidade
classesD = [0, 10, 30, 100, 300, 500]
classes2D = ['Até 10', '10-30', '30-100', '100-300', '300+']
Arquivo['Classe Densidade'] = pd.cut(Arquivo['Densidade'], bins=classesD, labels=classes2D)

# Calcula as frequencias
frequencia_populacao = Arquivo['Classe Populacao'].value_counts().sort_index()
frequencia_densidade = Arquivo['Classe Densidade'].value_counts().sort_index()

print("\nDistribuição de Frequência da População:")
print(frequencia_populacao)

print("\nDistribuição de Frequência da Densidade:")
print(frequencia_densidade)
