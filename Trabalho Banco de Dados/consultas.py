import sqlite3

def conectar():
    return sqlite3.connect("SuperMercado_SupriBem.db")

def consulta_pedidos_clientes():
    """
    JOIN entre Pedidos e Clientes
    Mostra id do pedido, data, vendedor, e nome do cliente
    """
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT Pedidos.id, Pedidos.data, Pedidos.vendedor, Clientes.nome
        FROM Pedidos
        JOIN Clientes ON Pedidos.cliente_id = Clientes.id
        ORDER BY Pedidos.data DESC
        LIMIT 10;  -- Usando LIMIT aqui
    """)
    resultados = cursor.fetchall()
    con.close()
    return resultados

def consulta_itens_produtos_pedidos():
    """
    JOIN entre ItensPedido, Produtos e Pedidos
    Mostra id do item, nome do produto, quantidade, valor unitário, data do pedido
    """
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT ItensPedido.id, Produtos.nome, ItensPedido.quantidade, ItensPedido.valor_unitario, Pedidos.data
        FROM ItensPedido
        JOIN Produtos ON ItensPedido.produto_id = Produtos.id
        JOIN Pedidos ON ItensPedido.pedido_id = Pedidos.id
        ORDER BY Pedidos.data DESC
        LIMIT 35;  -- Segundo uso de LIMIT
    """)
    resultados = cursor.fetchall()
    con.close()
    return resultados

def consulta_filtrar_cliente(nome_cliente):
    """
    Consulta com WHERE e LIKE para filtrar pedidos por nome do cliente
    """
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT Pedidos.id, Pedidos.data, Pedidos.vendedor, Clientes.nome
        FROM Pedidos
        JOIN Clientes ON Pedidos.cliente_id = Clientes.id
        WHERE Clientes.nome LIKE ?
        ORDER BY Pedidos.data DESC
    """, ('%' + nome_cliente + '%',))
    resultados = cursor.fetchall()
    con.close()
    return resultados

def consulta_filtrar_data(data_inicio, data_fim):
    """
    Consulta com WHERE para filtrar pedidos entre datas
    Datas no formato 'YYYY-MM-DD'
    """
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT Pedidos.id, Pedidos.data, Pedidos.vendedor, Clientes.nome
        FROM Pedidos
        JOIN Clientes ON Pedidos.cliente_id = Clientes.id
        WHERE date(Pedidos.data) BETWEEN date(?) AND date(?)
        ORDER BY Pedidos.data DESC
    """, (data_inicio, data_fim))
    resultados = cursor.fetchall()
    con.close()
    return resultados

def consulta_filtrar_produto(nome_produto):
    """
    Consulta com WHERE e JOIN para filtrar itens pelo nome do produto
    """
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT ItensPedido.id, Produtos.nome, ItensPedido.quantidade, ItensPedido.valor_unitario, Pedidos.data
        FROM ItensPedido
        JOIN Produtos ON ItensPedido.produto_id = Produtos.id
        JOIN Pedidos ON ItensPedido.pedido_id = Pedidos.id
        WHERE Produtos.nome LIKE ?
        ORDER BY Pedidos.data DESC
    """, ('%' + nome_produto + '%',))
    resultados = cursor.fetchall()
    con.close()
    return resultados

# ----------------------
# Exemplo de uso:
# ----------------------

if __name__ == "__main__":
    print("10 Pedidos com Clientes (LIMIT 10):")
    for pedido in consulta_pedidos_clientes():
        print(pedido)

    print("\n35 Itens do Pedido com Produtos e Datas (LIMIT 35):")
    for item in consulta_itens_produtos_pedidos():
        print(item)

    cliente = input("\nFiltrar pedidos pelo nome do cliente (use parte do nome): ")
    resultados_cliente = consulta_filtrar_cliente(cliente)
    print(f"\nPedidos para clientes com nome parecido a '{cliente}':")
    for r in resultados_cliente:
        print(r)

    data_inicio = input("\nFiltrar pedidos a partir de data (YYYY-MM-DD): ")
    data_fim = input("Até data (YYYY-MM-DD): ")
    resultados_data = consulta_filtrar_data(data_inicio, data_fim)
    print(f"\nPedidos entre {data_inicio} e {data_fim}:")
    for r in resultados_data:
        print(r)

    produto = input("\nFiltrar itens pelo nome do produto (use parte do nome): ")
    resultados_produto = consulta_filtrar_produto(produto)
    print(f"\nItens com produto parecido a '{produto}':")
    for r in resultados_produto:
        print(r)