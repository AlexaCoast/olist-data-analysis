import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


# 1. CONFIGURAÇÃO DA CONEXÃO COM O BANCO DE DADOS
SERVIDOR = 'SEU_SERVIDOR'  # PODE SER LOCALHOST OU O IP DO SERVIDOR
BANCO = 'OLIST'  # NOME DO BANCO DE DADOS
USUARIO = ('DB_USER')  # A VARIÁVEL DE AMBIENTE PARA O NOME DE USUÁRIO
SENHA = ('DB_PASSWORD')  # A VARIÁVEL DE AMBIENTE PARA A SENHA

# STRING DE CONEXÃO COM O BANCO DE DADOS SQL SERVER
CONN = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                      f'SERVER={SERVIDOR};'
                      f'DATABASE={BANCO};'
                      f'UID={USUARIO};'
                      f'PWD={SENHA}')

# VERIFICANDO SE A CONEXÃO FOI BEM-SUCEDIDA
print("CONEXÃO ESTABELECIDA COM SUCESSO!")

# 2. FUNÇÃO PARA EXECUTAR CONSULTAS SQL E RETORNAR COMO DATAFRAME
def query_to_dataframe(query):
    return pd.read_sql(query, CONN)

# 3. CONSULTA SQL PARA OBTER INFORMAÇÕES DE VENDAS POR VENDEDOR
QUERY_VENDAS_POR_VENDEDOR = """
SELECT 
    OI.SELLER_ID,
    COUNT(DISTINCT OI.ORDER_ID) AS TOTAL_PEDIDOS,
    SUM(CAST(OI.PRICE AS DECIMAL(10,2))) AS TOTAL_VENDIDO,
    SUM(CAST(OI.FREIGHT_VALUE AS DECIMAL(10,2))) AS TOTAL_FRETE
FROM TB_FACT_OLIST_ORDER_ITEMS OI
GROUP BY OI.SELLER_ID
"""

# EXECUTANDO A CONSULTA E ARMAZENANDO OS RESULTADOS NO DATAFRAME
DF_VENDAS_POR_VENDEDOR = query_to_dataframe(QUERY_VENDAS_POR_VENDEDOR)

# EXIBINDO AS PRIMEIRAS LINHAS DO DATAFRAME PARA VERIFICAR OS DADOS
print(DF_VENDAS_POR_VENDEDOR.head())

# 4. VISUALIZAÇÃO DOS DADOS - GRÁFICO DE BARRAS
plt.figure(figsize=(10, 6))  # TAMANHO DA FIGURA (OPCIONAL)
plt.bar(DF_VENDAS_POR_VENDEDOR['SELLER_ID'], DF_VENDAS_POR_VENDEDOR['TOTAL_VENDIDO'], color='skyblue')
plt.xlabel('VENDEDOR ID')
plt.ylabel('TOTAL VENDIDO')
plt.title('VENDAS POR VENDEDOR')
plt.xticks(rotation=90)  # ROTACIONA OS RÓTULOS DOS VENDENDORES PARA MELHOR VISUALIZAÇÃO
plt.show()
