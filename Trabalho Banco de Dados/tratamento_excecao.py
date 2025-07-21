import sqlite3

def inserir_cliente_com_nome_null():
    conexao = sqlite3.connect("SuperMercado_SupriBem.db")
    cursor = conexao.cursor()
    try:
        # nome é campo obrigatório (NOT NULL), passar None vai gerar IntegrityError
        cursor.execute("INSERT INTO Clientes (nome, email, cidade, telefone) VALUES (?, ?, ?, ?);",
                       (None, "teste@teste.com", "Cidade", "123456789"))
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print("Erro de integridade ao inserir cliente com nome NULL:", e)
    finally:
        conexao.close()

def registrar_venda_cliente_inexistente():
    conexao = sqlite3.connect("SuperMercado_SupriBem.db")
    cursor = conexao.cursor()
    try:
        # Tentar inserir pedido com cliente_id inexistente (ex: 999999)
        cursor.execute("INSERT INTO Pedidos (data, vendedor, cliente_id) VALUES (?, ?, ?);",
                       ("2025-07-21 10:00:00", "Vendedor 🍷🗿", 999999))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Falha: Cliente não encontrado para registrar a venda.")
    finally:
        conexao.close()

def executar_sql_incorreta():
    conexao = sqlite3.connect("SuperMercado_SupriBem.db")
    cursor = conexao.cursor()
    try:
        # Comando SQL com erro de digitação: "UPDAT" ao invés de "UPDATE"
        cursor.execute("UPDAT Clientes SET email = 'novo@email.com' WHERE id = 1;")
        conexao.commit()
    except sqlite3.OperationalError as e:
        print("Erro operacional: comando SQL incorreto.", e)
    finally:
        conexao.close()

if __name__ == "__main__":
    print("Teste 1: Inserir cliente com nome NULL")
    inserir_cliente_com_nome_null()

    print("\nTeste 2: Registrar venda com cliente inexistente")
    registrar_venda_cliente_inexistente()

    print("\nTeste 3: Executar SQL incorreto")
    executar_sql_incorreta()
