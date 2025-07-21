import sqlite3

def conectar():
    return sqlite3.connect("SuperMercado_SupriBem.db")

def alterar_email_cliente(cliente_id, novo_email):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, cliente_id))
    con.commit()
    con.close()
    print(f"E-mail do cliente {cliente_id} alterado para {novo_email}")

def excluir_pedido(pedido_id):
    con = conectar()
    cursor = con.cursor()
    # Para manter integridade, deletar itens do pedido antes
    cursor.execute("DELETE FROM ItensPedido WHERE pedido_id = ?", (pedido_id,))
    cursor.execute("DELETE FROM Pedidos WHERE id = ?", (pedido_id,))
    con.commit()
    con.close()
    print(f"Pedido {pedido_id} e seus itens foram excluídos.")

def excluir_item_pedido(item_id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM ItensPedido WHERE id = ?", (item_id,))
    con.commit()
    con.close()
    print(f"Item do pedido {item_id} excluído.")

if __name__ == "__main__":
    print("=== Atualizar e-mail do cliente ===")
    cliente_id = int(input("Digite o ID do cliente para alterar o e-mail: "))
    novo_email = input("Digite o novo e-mail: ")
    alterar_email_cliente(cliente_id, novo_email)

    print("\n=== Excluir pedido ===")
    pedido_id = int(input("Digite o ID do pedido para excluir: "))
    excluir_pedido(pedido_id)

    print("\n=== Excluir item do pedido ===")
    item_id = int(input("Digite o ID do item do pedido para excluir: "))
    excluir_item_pedido(item_id)
