import sqlite3

connection = sqlite3.connect('SuperMercado_SupriBem.db')
cursor = connection.cursor()

Clientes = [
    ('João Silva', 'joao.silva@email.com', 'São Paulo', '(11) 99999-1234', '123.456.789-00'),
    ('Maria Oliveira', 'maria.oliveira@email.com', 'Rio de Janeiro', '(21) 98888-4321', '234.567.890-11'),
    ('Carlos Souza', 'carlos.souza@email.com', 'Belo Horizonte', '(31) 97777-1234', '345.678.901-22'),
    ('Fernanda Lima', 'fernanda.lima@email.com', 'Curitiba', '(41) 96666-2345', '456.789.012-33'),
    ('Pedro Rocha', 'pedro.rocha@email.com', 'Porto Alegre', '(51) 95555-3456', '567.890.123-44'),
    ('Ana Costa', 'ana.costa@email.com', 'Fortaleza', '(85) 94444-4567', '678.901.234-55'),
    ('Luiz Pereira', 'luiz.pereira@email.com', 'Salvador', '(71) 93333-5678', '789.012.345-66'),
    ('Juliana Martins', 'juliana.martins@email.com', 'Recife', '(81) 92222-6789', '890.123.456-77'),
    ('Felipe Santos', 'felipe.santos@email.com', 'Manaus', '(92) 91111-7890', '901.234.567-88'),
    ('Carla Mendes', 'carla.mendes@email.com', 'Brasília', '(61) 90000-8901', '012.345.678-99'),
    ('Ricardo Almeida', 'ricardo.almeida@email.com', 'São Paulo', '(11) 98888-9012', '123.456.789-00'),
    ('Patrícia Costa', 'patricia.costa@email.com', 'Rio de Janeiro', '(21) 97777-0123', '234.567.890-11'),
    ('Marcos Oliveira', 'marcos.oliveira@email.com', 'Belo Horizonte', '(31) 96666-1234', '345.678.901-22'),
    ('Beatriz Silva', 'beatriz.silva@email.com', 'Curitiba', '(41) 95555-2345', '456.789.012-33'),
    ('Gustavo Rocha', 'gustavo.rocha@email.com', 'Porto Alegre', '(51) 94444-3456', '567.890.123-44'),
    ('Tatiane Souza', 'tatiane.souza@email.com', 'Fortaleza', '(85) 93333-4567', '678.901.234-55'),
    ('José Lima', 'jose.lima@email.com', 'Salvador', '(71) 92222-5678', '789.012.345-66'),
    ('Sandra Pereira', 'sandra.pereira@email.com', 'Recife', '(81) 91111-6789', '890.123.456-77'),
    ('Eduardo Martins', 'eduardo.martins@email.com', 'Manaus', '(92) 90000-7890', '901.234.567-88'),
    ('Aline Mendes', 'aline.mendes@email.com', 'Brasília', '(61) 98888-8901', '012.345.678-99'),
    ('Ricardo Costa', 'ricardo.costa@email.com', 'São Paulo', '(11) 97777-9012', '123.456.789-00'),
    ('Mariana Almeida', 'mariana.almeida@email.com', 'Rio de Janeiro', '(21) 96666-0123', '234.567.890-11'),
    ('Lucas Oliveira', 'lucas.oliveira@email.com', 'Belo Horizonte', '(31) 95555-1234', '345.678.901-22'),
    ('Isabela Silva', 'isabela.silva@email.com', 'Curitiba', '(41) 94444-2345', '456.789.012-33'),
    ('Fábio Rocha', 'fabio.rocha@email.com', 'Porto Alegre', '(51) 93333-3456', '567.890.123-44'),
    ('Larissa Souza', 'larissa.souza@email.com', 'Fortaleza', '(85) 92222-4567', '678.901.234-55'),
    ('Eduardo Lima', 'eduardo.lima@email.com', 'Salvador', '(71) 91111-5678', '789.012.345-66'),
    ('Paula Pereira', 'paula.pereira@email.com', 'Recife', '(81) 90000-6789', '890.123.456-77'),
    ('André Martins', 'andre.martins@email.com', 'Manaus', '(92) 98888-7890', '901.234.567-88'),
    ('Cláudia Mendes', 'claudia.mendes@email.com', 'Brasília', '(61) 97777-8901', '012.345.678-99'),
]

# Lista de 30 produtos
Produtos = [
    ('Produto A', 19.90, 'Eletrodomésticos'),
    ('Produto B', 49.90, 'Informática'),
    ('Produto C', 199.90, 'Eletrodomésticos'),
    ('Produto D', 99.90, 'Eletrônicos'),
    ('Produto E', 29.90, 'Móveis'),
    ('Produto F', 15.90, 'Eletrodomésticos'),
    ('Produto G', 79.90, 'Automotivo'),
    ('Produto H', 10.90, 'Alimentos'),
    ('Produto I', 250.00, 'Ferramentas'),
    ('Produto J', 69.90, 'Moda'),
    ('Produto K', 9.90, 'Brinquedos'),
    ('Produto L', 34.90, 'Eletrodomésticos'),
    ('Produto M', 179.90, 'Móveis'),
    ('Produto N', 39.90, 'Eletrônicos'),
    ('Produto O', 99.90, 'Tecnologia'),
    ('Produto P', 59.90, 'Fitness'),
    ('Produto Q', 129.90, 'Automotivo'),
    ('Produto R', 199.90, 'Eletrodomésticos'),
    ('Produto S', 5.90, 'Alimentos'),
    ('Produto T', 159.90, 'Moda'),
    ('Produto U', 45.90, 'Eletrodomésticos'),
    ('Produto V', 89.90, 'Esportes'),
    ('Produto W', 120.00, 'Informática'),
    ('Produto X', 89.00, 'Brinquedos'),
    ('Produto Y', 15.00, 'Cosméticos'),
    ('Produto Z', 30.00, 'Fitness'),
    ('Produto AA', 10.00, 'Saúde'),
    ('Produto BB', 25.00, 'Alimentos'),
    ('Produto CC', 75.00, 'Tecnologia'),
    ('Produto DD', 140.00, 'Ferramentas'),
    ('Produto EE', 50.00, 'Moda'),
]

# Lista de 10 pedidos
Pedidos = [
    ('2023-07-01', 1, 1),
    ('2023-07-02', 2, 2),
    ('2023-07-03', 3, 3),
    ('2023-07-04', 4, 4),
    ('2023-07-05', 5, 5),
    ('2023-07-06', 6, 6),
    ('2023-07-07', 7, 7),
    ('2023-07-08', 8, 8),
    ('2023-07-09', 9, 9),
    ('2023-07-10', 10, 10),
]

# Itens dos pedidos
itens_pedido = [
    (1, 1, 2), (1, 2, 1), (1, 3, 1),
    (2, 4, 1), (2, 5, 2),
    (3, 6, 1), (3, 7, 3), (3, 8, 2),
    (4, 9, 1), (4, 10, 1),
    (5, 11, 2), (5, 12, 1),
    (6, 13, 3), (6, 14, 2),
    (7, 15, 1), (7, 16, 1),
    (8, 17, 2), (8, 18, 1),
    (9, 19, 1), (9, 20, 2),
    (10, 21, 2), (10, 22, 1),
]

# Função para inserir clientes
def inserir_clientes():
    cursor.executemany(''' 
    INSERT INTO Clientes (nome, email, cidade, telefone, cpf) VALUES (?, ?, ?, ?, ?)
    ''', Clientes)
    print(f"{len(Clientes)} clientes inseridos com sucesso!")

# Função para inserir produtos
def inserir_produtos():
    cursor.executemany(''' 
    INSERT INTO Produtos (nome, preco, categoria) VALUES (?, ?, ?)
    ''', Produtos)
    print(f"{len(Produtos)} produtos inseridos com sucesso!")

# Função para inserir pedidos
def inserir_pedidos():
    cursor.executemany(''' 
    INSERT INTO pedidos (data_compra, id_vendedor, id_cliente) VALUES (?, ?, ?)
    ''', Pedidos)
    print(f"{len(Pedidos)} pedidos inseridos com sucesso!")

# Função para inserir itens de pedidos
def inserir_itens_pedido():
    cursor.executemany(''' 
    INSERT INTO Pedidos (id_pedido, id_produto, quantidade) VALUES (?, ?, ?)
    ''', itens_pedido)
    print(f"{len(itens_pedido)} itens de pedido inseridos com sucesso!")

# Função principal
def main():
    inserir_clientes()
    inserir_produtos()
    inserir_pedidos()
    inserir_itens_pedido()
    connection.commit()  # Confirmar as transações no banco de dados
    connection.close()  # Fechar a conexão com o banco de dados
    print("Todos os dados foram inseridos com sucesso!")

if __name__ == "__main__":
    main()
