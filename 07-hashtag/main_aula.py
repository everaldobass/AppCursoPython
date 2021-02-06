import pandas as pd
from twilio.rest import Client
# Inseri as informações da conta
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Inserir as informações do token
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
 #Conectando no Twilio

# Instalação Bibliotecas Python3
# Passo a Passo
# Abrir os arquivos de excel criando uma lista de meses
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# utilizar um For para abrir os arquivos
for mes in lista_meses:
    # print(mes)
 # Read lê a extenção do arquivo da planilha que deseja utilizar
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Mostrar o arquivo da tabela vendas.
# print(tabela_vendas)
# Fim do For
# Para cada arquivo:
    # Verificar se os valores na colone de vendas e maior que 55.000
    if (tabela_vendas['Vendas'] > 30000).any():

        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendas'].values[0]

        print(f' No mês de { mes},  O Vendedor: {vendedor},  Vendas: {vendas}')
        # Se for maior que 55 mil envia um SMS com o nome, o mês e as vendas do vendendor.
        message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body=f' No mês de { mes},  O Vendedor: {vendedor},  Vendas: {vendas}')

        print(message.sid)

# caso seja menor não faz nada.
