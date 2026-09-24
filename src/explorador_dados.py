import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # exibe todas as colunas no print, sem truncar com "..."

df = pd.read_csv("dataraw/wter-evkm_version_57907.csv")  # carrega o CSV bruto como DataFrame

print(df.columns.tolist())  # lista os nomes reais das colunas do CSV original

vet_df = df.rename(columns={'datatime2' : 'data_e_hora_2', 'datatime' : 'data_e_hora', 'animal_id' : 'id_animal', 'name' : 'nome', 'found_location' : 'Local encontrado', 'intake_type' : 'tipo_de_entrada', 'intake_condition' : 'condicao_de_entrada','animal_type' : 'tipo_de_animal', 'sex_upon_intake' : 'sexo_na_entrada', 'age_upon_intake': 'idade_na_entrada', 'breed' : 'raca', 'color': 'cor'})
# cria vet_df como cópia de df com as colunas renomeadas pra português (df original permanece intacto)

vet_df.info()  # mostra tipo de dado e contagem de não-nulos por coluna

vet_df.copy()  # não tem efeito: cria uma cópia mas não é atribuída a nenhuma variável

#for colunas in vet_df.columns:
    #print(colunas)
    #print(vet_df[colunas].unique())
    #print('\n\n')
    #print(vet_df[colunas].value_counts())
    #print('\n\n')
    #print('------------------------------------------------------------')
    #print('\n\n')
# bloco de exploração manual (valores únicos e contagens por coluna), deixado comentado após uso

for colunas in vet_df.select_dtypes(include='str').columns:
   vet_df[colunas] = vet_df[colunas].str.strip()
   # para cada coluna de texto, remove espaços sobrando no início/fim de cada valor

print(pd.isnull(vet_df).sum().tolist())  # diagnóstico "antes": total de nulos por coluna

values = {'nome': 'Desconhecido', 'Local encontrado': 'Desconhecido', 'tipo_de_entrada': 'Desconhecido', 'condicao_de_entrada': 'Desconhecido', 'tipo_de_animal': 'Desconhecido', 'sexo_na_entrada': 'Desconhecido', 'idade_na_entrada': 'Desconhecido', 'raca': 'Desconhecido', 'cor': 'Desconhecido'}
# dicionário: para cada coluna, o valor que deve substituir os nulos encontrados nela

vet_df = vet_df.fillna(value=values)  # aplica o preenchimento de nulos conforme o dicionário acima
print(pd.isnull(vet_df).sum().tolist())  # diagnóstico "depois": confirma que os nulos foram tratados

vet_df = vet_df.drop_duplicates()  # remove linhas totalmente duplicadas (todas as colunas iguais)

print(vet_df.duplicated().sum())  # conta duplicados restantes (roda depois do drop, por isso tende a 0)

vet_df[['numero_idade', 'unidade_idade']] = vet_df['idade_na_entrada'].str.split(' ', expand=True)
# separa "idade_na_entrada" (ex: "6 years") em duas colunas novas: número e unidade

print(vet_df[['idade_na_entrada', 'numero_idade', 'unidade_idade']].head(10))  # confere a separação

print(vet_df['unidade_idade'].unique())  # lista as variações de unidade encontradas (year, years, etc)

vet_df['numero_idade'] = pd.to_numeric(vet_df['numero_idade'], errors='coerce')
# converte a coluna de texto para número; valores que não convertem viram NaN em vez de quebrar o script



linhas_negativas = vet_df[vet_df['numero_idade'] < 0]
print(linhas_negativas[['idade_na_entrada', 'numero_idade', 'unidade_idade']])

print(vet_df['numero_idade'].unique())  # só mostra os valores negativos, já que vet_df foi reduzido acima
vet_df.info()  # por isso aqui aparecem só as poucas linhas negativas, não a base inteira

vet_df['unidade_idade'] = vet_df['unidade_idade'].str.rstrip('s')  # remove "s" final (plural → singular)

print(vet_df['unidade_idade'].unique())