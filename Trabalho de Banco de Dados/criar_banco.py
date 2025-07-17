import sqlite3

connection = sqlite3.connect('SuperMercado_SupriBem.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cidade TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cpf TEXT NOT NULL
               
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra TEXT NOT NULL,
    id_vendedor INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ItensPedido (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);
''')

connection.commit()

connection.close()

print("Banco de dados e tabelas criados com sucesso!")
