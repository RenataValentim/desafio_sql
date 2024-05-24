
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