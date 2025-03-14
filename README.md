# Projeto de Análise de Dados - Olist (Kaggle)

## Descrição do Projeto
Este projeto tem como objetivo realizar uma análise detalhada de dados utilizando o banco de dados do Olist, disponível no Kaggle. A análise foi realizada com o uso do SQL Server para modelagem do banco de dados, bem como Python (com pandas) para manipulação e visualização dos dados. O projeto inclui importação de bases de dados, criação de tabelas de carga, tabelas de fatos, relacionamentos, joins, visualizações e geração de insights a partir dos dados.

## Tecnologias Utilizadas
- **SQL Server**: Utilizado para criar o banco de dados, tabelas, visualizações e executar consultas SQL.
- **Python (pandas)**: Utilizado para importar, manipular e visualizar os dados.
- **Matplotlib**: Para a criação de gráficos e visualizações.

## Etapas do Processo

## Criação e Configuração do Banco de Dados no SQL Server
O banco de dados foi criado no SQL Server com o seguinte código:

```sql
CREATE DATABASE OLIST  
ON PRIMARY  
(  
    NAME = OLIST,  
    FILENAME = 'C:\SQL_SERVER\BASE.MDF',  
    SIZE = 6MB,  
    FILEGROWTH = 2MB  
)  
LOG ON  
(  
    NAME = OLIST_LOG,  
    FILENAME = 'C:\SQL_SERVER\BASE.LDF',  
    SIZE = 10MB,  
    MAXSIZE = 50MB,  
    FILEGROWTH = 5MB  
);

```
## Criação das Tabelas de Carga e Fato
As tabelas de carga e fato foram criadas com os seguintes exemplos:

```sql
CREATE TABLE TB_OLIST_PRODUCTS (
    PRODUCT_ID VARCHAR(150) PRIMARY KEY,
    PRODUCT_CATEGORY_NAME VARCHAR(MAX),
    ...
);

CREATE TABLE TB_FACT_OLIST_GEOLOCATION (
    GEOLOCATION_ZIP_CODE_PREFIX VARCHAR(50),
    GEOLOCATION_LAT VARCHAR(100),
    ...
);
```

## Importação de Dados
O processo de importação foi realizado utilizando o comando BULK INSERT:

```sql
BULK INSERT TB_OLIST_ORDERS
FROM 'C:\SQL_SERVER\base\planilhas\olist_orders_dataset.csv'
WITH (
    FIRSTROW = 2,  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '0x0A',
    TABLOCK
);

```

## Criação de Views para Análise
Foram criadas diversas visualizações para facilitar a análise dos dados, como a análise de vendas por vendedor:

```sql
CREATE VIEW VW_VENDAS_POR_VENDEDOR AS
SELECT 
    OI.SELLER_ID, 
    COUNT(DISTINCT OI.ORDER_ID) AS TOTAL_PEDIDOS,
    ...
FROM TB_FACT_OLIST_ORDER_ITEMS OI
GROUP BY OI.SELLER_ID;

```


## Análise de Dados com Python (pandas)
Com a conexão estabelecida com o banco de dados no Python, as consultas SQL foram realizadas e os dados manipulados.
Exemplo de código para análise de vendas por vendedor:

```python
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Conexão com o SQL Server
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                      f'SERVER={servidor};'
                      f'DATABASE={banco};'
                      f'UID={usuario};'
                      f'PWD={senha}')

# Função para consulta SQL e retorno como DataFrame
def query_to_dataframe(query):
    return pd.read_sql(query, conn)

# Exemplo de consulta para vendas por vendedor
df_vendas_por_vendedor = query_to_dataframe(query_vendas_por_vendedor)

# Visualização com Matplotlib
plt.bar(df_vendas_por_vendedor['SELLER_ID'], df_vendas_por_vendedor['TOTAL_VENDIDO'])
plt.show()
```


## Resultados e Visualizações
Através do uso do Matplotlib, foram gerados gráficos para visualização dos dados, como análise das vendas por vendedor, tempo de entrega, entre outros.

## Conclusão
Este projeto exemplifica como é possível utilizar SQL Server e Python para análise de grandes volumes de dados, com foco em vendas, desempenho de vendedores, análise de tempo de entrega e outros KPIs importantes. 
As consultas SQL otimizadas e as visualizações interativas ajudam a fornecer insights importantes para decisões estratégicas.


