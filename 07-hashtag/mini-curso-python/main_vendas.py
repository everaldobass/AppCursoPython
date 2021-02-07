# Aula 03 - Lógica de programação

# Aula 04 - immportar as bibliotecas
import pandas as pd
# Aula 05 - Importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')
# Aula 06 - Visualisar a base de dados

print("\n ===================  Visualisa os dados da Tabela de Vendas: =====================================================\n")
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# Aula 07 - Métodos e Filtro de agrupamento Faturamento por loja
print("\n =========== Primeiro Filtro, Data, Quantidade de Lojas: ===========================================================\n")
filtro1 = tabela_vendas[['Data', 'Código Venda', 'ID Loja']]
print(filtro1)

# Aula 07 -Agrupando as lojas da tabela de vendas
print("\n =========== Segundo Filtro, ID Loja,  e Valor Final por Lojas: ==================================================\n")
valor = tabela_vendas[['Data', 'Código Venda',
                       'ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(valor)

# Tabela venda id loja e valor final
print("\n ============ Terceiro Faturamento Final por Lojas: =============================================================\n")
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby(
    'ID Loja').sum()
print(faturamento)

# Aula 08 - Quantidade de produtos vendidos por loja
print("\n ============= Segundo Relatório Quntidade de Produtos por Lojas: ================================================\n")
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

#  Aula 9 - Tiket Média por loja
print("\n ================================== Tiket Média por cada Loja: ===================================================\n")
# To_Frame para formatar uma tabela
ticket_medio = (faturamento['Valor Final'] /
                quantidade['Quantidade']).to_frame()
print(ticket_medio)
