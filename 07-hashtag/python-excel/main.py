
import pandas as pd
from twilio.rest import Client
"""
Arquivo principal desenvolvido na alua.
"""

# Abrir os arquivos de excel criando uma lista de meses
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
# utilizar um For para abrir os arquivos
for mes in lista_meses:
# print(mes)
#Read lê a extenção do arquivo da planilha que deseja utilizar
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Mostrar o arquivo da tabela vendas.
    print(tabela_vendas)
    # Verificar se os valores na colone de vendas e maior que 55.000
    if (tabela_vendas['Vendas'] > 30000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendas'].values[0]
         # Se for maior que 30 mil envia um SMS com o nome, o mês e as vendas do vendendor.
        print(f' No mês de { mes},  O Vendedor: {vendedor},  Vendas: {vendas}')
# caso seja menor não faz nada.
