import sqlite3

# Cria ou conecta ao banco de dados SQLite
conexao = sqlite3.connect("SuperMercado_SupriBem.db")
cursor = conexao.cursor()

# Tabela Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cidade TEXT,
    telefone TEXT
);
""")

# Tabela Produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT
);
""")

# Tabela Pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    vendedor TEXT NOT NULL,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);
""")

# Tabela ItensPedido (junção entre Pedidos e Produtos)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ItensPedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);
""")

# Salva as alterações e fecha a conexão
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
