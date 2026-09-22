import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv("dataraw/wter-evkm_version_57907.csv")







vet_df = df.rename(columns={'datatime2' : 'data_e_hora_2', 'datatime' : 'data_e_hora', 'animal_id' : 'id_animal', 'name' : 'nome', 'found_location' : 'Local encontrado', 'intake_type' : 'tipo_de_entrada', 'intake_condition' : 'condicao_de_entrada','animal_type' : 'tipo_de_animal', 'sex_upon_intake' : 'sexo_na_entrada', 'age_upon_intake': 'idade_na_entrada', 'breed' : 'raca', 'color': 'cor'})



#vet_df.info()

vet_df.copy()

#for colunas in vet_df.columns:
    #print(colunas)
    #print(vet_df[colunas].unique())
    #print('\n\n')
    #print(vet_df[colunas].value_counts())
    #print('\n\n')
    #print('------------------------------------------------------------')
    #print('\n\n')



for colunas in vet_df.select_dtypes(include='object').columns:
   vet_df[colunas] = vet_df[colunas].str.strip()



print(pd.isnull(vet_df).sum().tolist())


vet_df = vet_df.dropna(how='any', axis=0)

vet_df = vet_df.drop_duplicates()



print(pd.isnull(vet_df).sum().tolist())