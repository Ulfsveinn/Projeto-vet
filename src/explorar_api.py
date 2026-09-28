import requests

#url do IBGE para buscar os municípios do estado do Rio Grande do Sul (código 43)
url='https://servicodados.ibge.gov.br/api/v1/localidades/estados/43/municipios'



resposta=requests.get(url) # get request para a url
#print(resposta.status_code) # printar o status code da resposta
#print(resposta.json()) # printar o conteúdo da resposta em formato JSON



dados = resposta.json() # armazena o conteúdo da resposta em formato JSON na variável 'dados'


print(dados[0]['nome'])

quantidade_municipios = len(dados)-1 # calcula a quantidade de municípios retornados na resposta
print(f'Quantidade de municípios no estado do Rio Grande do Sul: {quantidade_municipios}') # printa a quantidade de municípios

for i in range(quantidade_municipios): 
    print(dados[i]['nome']) 
    
    




