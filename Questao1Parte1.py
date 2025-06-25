import pandas as pd

#Não foi usado o mesmo arquivo que Dados_EB pois as alterações sujavam os dados lidos por aqui, então o terminal ficava bugado 
arquivo = pd.ExcelFile('Dados_EB_py.xlsx')

# Para saber o nome exato de cada dataframe do arquivo
# print(arquivo.sheet_names)

df = arquivo.parse('Tabela 2.1', skiprows=1) # o nome da aba que tem os empregados

#print(df.columns) #Printa as planilhas dentro do dataframe (para debug)

# 1. Estado Civil
frequencia_estado_civil = df['Estado Civil'].value_counts() #Equivalente ao =Cont.se(x, y; "critério")
print("Distribuição de Frequência do Estado civil:")
print(frequencia_estado_civil)

# 2. Região de procedencia
frequencia_regiao = df['Região de Procedência'].value_counts()
print("\nDistribuição de Frequência da Região de procedência:")
print(frequencia_regiao)

# 3. Número de filhos dos empregados casados
casados = df[df['Estado Civil'] == 'casado']
frequencia_filhos_casados = casados['N de Filhos'].value_counts()
print("\nDistribuição de Frequência do Número de Filhos dos empregados casados):")
print(frequencia_filhos_casados)

# 4.2 Idade  (Anos + meses, resultando em um número decimal)
df['Idade'] = df['Anos'] + (df['Meses'] / 12) 
frequencia_idade = df['Idade'].value_counts().sort_index()
print("\nDistribuição de Frequência - Idade:")
print(frequencia_idade)

# 4. Frequência de Anos
# frequencia_anos = df['Anos'].value_counts().sort_index()
# print(frequencia_anos)

# 4.1 Frequência de Meses
# frequencia_meses = df['Meses'].value_counts().sort_index()
# print(frequencia_meses)






