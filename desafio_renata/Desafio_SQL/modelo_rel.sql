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