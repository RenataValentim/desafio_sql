import pandas as pd

# carregamento do arquivo.csv junto com sua delimitação por ';' 
df = pd.read_csv('DB_Teste.csv', delimiter=';')


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

