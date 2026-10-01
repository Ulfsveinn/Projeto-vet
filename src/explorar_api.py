import requests
import pandas as pd
#url do IBGE para buscar os municípios do estado do Rio Grande do Sul (código 43)
url='https://servicodados.ibge.gov.br/api/v1/localidades/estados/43/municipios'



resposta=requests.get(url) # get request para a url
#print(resposta.status_code) # printar o status code da resposta
#print(resposta.json()) # printar o conteúdo da resposta em formato JSON



dados = resposta.json() # armazena o conteúdo da resposta em formato JSON na variável 'dados'


print(dados[0])

quantidade_municipios = len(dados)# calcula a quantidade de municípios retornados na resposta
print(f'Quantidade de municípios no estado do Rio Grande do Sul: {quantidade_municipios}') # printa a quantidade de municípios


#imprimi todos os municipios pelo nome
#for municipio in dados:
    #print(municipio['nome'])


df = pd.DataFrame(dados)
print(df.shape)
print(df.columns)

print(df['microrregiao'].iloc[0]['id'])
print(df['regiao-imediata'].iloc[0]['id'])

#total_duplicadas = df.duplicated().sum() #gera todos os dados duplicados 

#print(f'Total de registros duplicados: {total_duplicadas}') print os dados duplicados


df_normalizados = pd.json_normalize(dados) # dados normalizados, todos os dados eram dict(Dicionarios) e agora viraram colunas para facilitar e poder utilizar o df.duplicated().sum()

print(df_normalizados.shape)

print(df_normalizados.columns)

print(df_normalizados.dtypes)