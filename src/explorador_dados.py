import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv("dataraw/wter-evkm_version_57907.csv")

print(df.columns.tolist())







vet_df = df.rename(columns={'datatime2' : 'data_e_hora_2', 'datatime' : 'data_e_hora', 'animal_id' : 'id_animal', 'name' : 'nome', 'found_location' : 'Local encontrado', 'intake_type' : 'tipo_de_entrada', 'intake_condition' : 'condicao_de_entrada','animal_type' : 'tipo_de_animal', 'sex_upon_intake' : 'sexo_na_entrada', 'age_upon_intake': 'idade_na_entrada', 'breed' : 'raca', 'color': 'cor'})



vet_df.info()

vet_df.copy()

#for colunas in vet_df.columns:
    #print(colunas)
    #print(vet_df[colunas].unique())
    #print('\n\n')
    #print(vet_df[colunas].value_counts())
    #print('\n\n')
    #print('------------------------------------------------------------')
    #print('\n\n')



for colunas in vet_df.select_dtypes(include='str').columns:
   vet_df[colunas] = vet_df[colunas].str.strip()



print(pd.isnull(vet_df).sum().tolist())

values = {'nome': 'Desconhecido', 'Local encontrado': 'Desconhecido', 'tipo_de_entrada': 'Desconhecido', 'condicao_de_entrada': 'Desconhecido', 'tipo_de_animal': 'Desconhecido', 'sexo_na_entrada': 'Desconhecido', 'idade_na_entrada': 'Desconhecido', 'raca': 'Desconhecido', 'cor': 'Desconhecido'}

vet_df = vet_df.fillna(value=values)
print(pd.isnull(vet_df).sum().tolist())

vet_df = vet_df.drop_duplicates()

print(vet_df.duplicated().sum())



vet_df[['numero_idade', 'unidade_idade']] = vet_df['idade_na_entrada'].str.split(' ', expand=True)


print(vet_df[['idade_na_entrada', 'numero_idade', 'unidade_idade']].head(10))


print(vet_df['unidade_idade'].unique())

vet_df['numero_idade'] = pd.to_numeric(vet_df['numero_idade'], errors='coerce')
vet_df = vet_df[vet_df['numero_idade'] < 0]
print(vet_df['numero_idade'].unique())
vet_df.info()


vet_df['unidade_idade'] = vet_df['unidade_idade'].str.rstrip('s')

print(vet_df['unidade_idade'].unique())