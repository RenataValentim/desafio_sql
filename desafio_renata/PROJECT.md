# Projeto de Processamento de Vendas e Consultas SQL

Este projeto envolve a implementação de um script Python para processar um arquivo CSV com informações de vendas e a criação de consultas SQL 

## Estrutura do Projeto

- `Desafio_python`: Script Python que processa o arquivo CSV e realiza tarefas de análise.
- `Desafio_SQL`: Arquivo com consultas SQL + imagens 
- `PROJECT.md`: Este arquivo com a documentação do projeto.


## Passos Realizados

### 1. Processamento de Vendas com Python

O script `Desafio_python` realiza as seguintes tarefas:
- Sumariza o valor vendido por cada vendedor
- Identifica o cliente responsável pela venda com maior valor e com menor valor
- Calcula o valor médio por tipo de venda (Serviços, Licenciamento, Produtos)
- Conta o número de vendas realizadas por cliente

#### Executando o Projeto

1. Importe a biblioteca 'pandas' para ler o arquivo CSV e então carregue os dados 
    ```bash
    # carregamento do arquivo.csv junto com sua delimitação por ';' 
    df = pd.read_csv('DB_Teste.csv', delimiter=';')
    ```

2. Para implementação dos dois primeiros desafios podemos seguir os passos abaixo:
    ```py
    # Para tabela auxiliar que sumariza o valor vendido por cada vendedor (ordenando do maior para o menor)
    vendas_por_vendedor = df.groupby('Vendedor')['Valor'].sum().reset_index().sort_values(by='Valor', ascending=False)
    print("Valor vendido por cada vendedor (do maior para o menor):")
    print(vendas_por_vendedor)

    # Indentificação do cliente responsável pela venda com maior valor e com menor valor
    venda_maxima = df.loc[df['Valor'].idxmax()]
    venda_minima = df.loc[df['Valor'].idxmin()]

    print("\nCliente responsável pela venda com maior valor:")
    print(f"Cliente: {venda_maxima['Cliente']}, Valor: {venda_maxima['Valor']}")

    print("\nCliente responsável pela venda com menor valor:")
    print(f"Cliente: {venda_minima['Cliente']}, Valor: {venda_minima['Valor']}")

    ```
3. Neste ponto devemos perceber que a coluna de consulta de Valor esta em VARCHAR e que não vamos conseguir trabalhar com estes dados nesta forma, estão devemos corrigir e dar sequencia ao desafio.:
   ```py
     # A Partir deste ponto o codigo dava erro, consegui resolver reorganizando a coluna Valor
    def limpar_valor(valor):
    """Remove o símbolo de moeda e converte para float"""
    return float(valor.replace('R$', '').replace('.', '').replace(',', '.').strip())

    try:
   
    # Limpar e converter a coluna de valores
    df['Valor'] = df['Valor'].apply(limpar_valor)

    # Padronizar a coluna Cliente (remover espaços extras)
    df['Cliente'] = df['Cliente'].str.strip()

    # Valor médio por Tipo de venda
    valor_medio_por_tipo = df.groupby('Tipo')['Valor'].mean()
    print("\nValor médio por Tipo de Venda:")
    print(valor_medio_por_tipo)

    # Número de vendas realizadas por cliente
    vendas_por_cliente = df['Cliente'].value_counts()
    print("\nNúmero de vendas realizadas por cliente:")
    print(vendas_por_cliente)


    except Exception as e:
    print(f"Erro inesperado: {e}")
   ```

### 2. Consultas SQL

O arquivo `Desafio_SQL` contém:
- Modelo de relacionamento e o digrama do modelo 
- Lista de todas as vendas (ID) e seus respectivos clientes no ano de 2020
- Lista das equipes de cada vendedor
- Construção de uma tabela que avalia trimestralmente o resultado de vendas e o plote do gráfico deste histórico


#### Executando o projeto

1. Primeiro construimos um modelo de relacionamento com o arquivo CSV ultilizando o SQL Server Management Studio (SSMS) e depois fazemos os relacionamentos entre as tabelas, baseados nas chaves primárias e estrangeiras. (imagem se encontra no arquivo `Desafio_SQL`)

```sql
-- Tabela Cliente
CREATE TABLE Cliente (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100)
);

-- Tabela Vendedor
CREATE TABLE Vendedor (
    VendedorID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Equipe VARCHAR(50)
);

-- Tabela Venda
CREATE TABLE Venda (
    VendaID INT PRIMARY KEY,
    ClienteID INT,
    VendedorID INT,
    DataDaVenda DATE,
    Tipo VARCHAR(50),
    Categoria VARCHAR(50),
    Regional VARCHAR(50),
    DuracaoContratoMeses INT,
    Valor DECIMAL(10, 2),

    CONSTRAINT FK_Venda_Cliente FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID),
    CONSTRAINT FK_Venda_Vendedor FOREIGN KEY (VendedorID) REFERENCES Vendedor(VendedorID)
);
```
2. Fazemos a importação do arquivo CVS no banco do SSMS e assim temos a tabela `dbo.DB_Teste` para fazer as consultas das vendas e clientes no ano de 2020, e então damos sequência ao desafio fazendo a equipe de cada vendedor e avaliação dos resultados trimestrais (devemos novamente fazer a correção do VARCHAR para DECIMAL na coluna Valor).  Com a tabela obtida foi exportado os dados em CVS para EXCEL e plotado o gráfico que se encontra no `Desafio_SQL`

```sql
   -- Consulta as vendas e clientes de 2020
SELECT *
FROM dbo.DB_Teste
WHERE YEAR([Data da Venda]) = 2020;

-- Lista da equipe de cada vendedor
SELECT Vendedor, Equipe
FROM dbo.DB_Teste
GROUP BY Vendedor, Equipe
ORDER BY Equipe;

-- Consulta para converter valores e avaliar resultados trimestrais, trocando o VARCHAR pelo DECIMAL para a realização da consulta
SELECT 
    YEAR([Data da Venda]) AS Ano,
    DATEPART(QUARTER, [Data da Venda]) AS Trimestre,
    SUM(CAST(REPLACE(REPLACE(REPLACE(Valor, 'R$', ''), '.', ''), ',', '.') AS DECIMAL(10, 2))) AS TotalVendas
FROM 
    dbo.DB_Teste
GROUP BY 
    YEAR([Data da Venda]), DATEPART(QUARTER, [Data da Venda])
ORDER BY 
    Ano, Trimestre;
```
## Agradecimento 

Quero agradecer pela oportunidade, foi um desafio agregador para meus conhecimentos!!
