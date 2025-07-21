import sqlite3
from datetime import datetime
import random

# Conectar ao banco de dados
conexao = sqlite3.connect("SuperMercado_SupriBem.db")
cursor = conexao.cursor()

# ------------------------- #
# 1. Inserir 30 CLIENTES    #
# ------------------------- #

clientes = [
    ("João Silva", "joao1@email.com", "São Paulo", "11999990001"),
    ("Maria Souza", "maria2@email.com", "Rio de Janeiro", "21999990002"),
    ("Carlos Lima", "carlos3@email.com", "Belo Horizonte", "31999990003"),
    ("Ana Costa", "ana4@email.com", "Curitiba", "41999990004"),
    ("Lucas Rocha", "lucas5@email.com", "Salvador", "71999990005"),
    ("Juliana Dias", "juliana6@email.com", "Fortaleza", "85999990006"),
    ("Bruno Mendes", "bruno7@email.com", "Brasília", "61999990007"),
    ("Fernanda Ramos", "fernanda8@email.com", "Manaus", "92999990008"),
    ("Marcos Teixeira", "marcos9@email.com", "Recife", "81999990009"),
    ("Camila Oliveira", "camila10@email.com", "Porto Alegre", "51999990010"),
    ("Thiago Martins", "thiago11@email.com", "São Paulo", "11999990011"),
    ("Patrícia Gomes", "patricia12@email.com", "Campinas", "19999990012"),
    ("Renato Alves", "renato13@email.com", "São Luís", "98999990013"),
    ("Larissa Pinto", "larissa14@email.com", "Maceió", "82999990014"),
    ("Felipe Souza", "felipe15@email.com", "Natal", "84999990015"),
    ("Aline Fernandes", "aline16@email.com", "Aracaju", "79999990016"),
    ("Diego Costa", "diego17@email.com", "Teresina", "86999990017"),
    ("Natália Lima", "natalia18@email.com", "João Pessoa", "83999990018"),
    ("Rafael Moraes", "rafael19@email.com", "Belém", "91999990019"),
    ("Isabela Nunes", "isabela20@email.com", "Florianópolis", "48999990020"),
    ("Gabriel Ribeiro", "gabriel21@email.com", "Vitória", "27999990021"),
    ("Viviane Borges", "viviane22@email.com", "São Paulo", "11999990022"),
    ("André Carvalho", "andre23@email.com", "Ribeirão Preto", "16999990023"),
    ("Beatriz Almeida", "beatriz24@email.com", "Santos", "13999990024"),
    ("Eduardo Silva", "eduardo25@email.com", "Bauru", "14999990025"),
    ("Letícia Vieira", "leticia26@email.com", "Sorocaba", "15999990026"),
    ("Fábio Freitas", "fabio27@email.com", "Uberlândia", "34999990027"),
    ("Tatiane Castro", "tatiane28@email.com", "Feira de Santana", "75999990028"),
    ("Marcelo Rocha", "marcelo29@email.com", "Cuiabá", "65999990029"),
    ("Sabrina Araújo", "sabrina30@email.com", "Joinville", "47999990030")
]

cursor.executemany("INSERT OR IGNORE INTO Clientes (nome, email, cidade, telefone) VALUES (?, ?, ?, ?);", clientes)


# ------------------------ #
# 2. Inserir 30 PRODUTOS   #
# ------------------------ #

produtos = [
    ("Arroz Tipo 1", 5.49, "Alimentos"),
    ("Feijão Carioca", 6.29, "Alimentos"),
    ("Macarrão Espaguete", 3.99, "Massas"),
    ("Leite Integral", 4.79, "Laticínios"),
    ("Queijo Mussarela", 29.99, "Laticínios"),
    ("Iogurte Morango", 2.50, "Laticínios"),
    ("Detergente Líquido", 1.99, "Limpeza"),
    ("Sabão em Pó", 7.99, "Limpeza"),
    ("Desinfetante", 3.49, "Limpeza"),
    ("Shampoo", 10.49, "Higiene"),
    ("Condicionador", 11.29, "Higiene"),
    ("Papel Higiênico", 12.99, "Higiene"),
    ("Óleo de Soja", 4.99, "Alimentos"),
    ("Açúcar Refinado", 3.89, "Alimentos"),
    ("Sal Refinado", 1.49, "Alimentos"),
    ("Refrigerante Cola", 6.49, "Bebidas"),
    ("Suco de Laranja", 5.99, "Bebidas"),
    ("Água Mineral", 1.29, "Bebidas"),
    ("Cerveja Lata", 2.99, "Bebidas"),
    ("Biscoito Recheado", 2.79, "Snacks"),
    ("Chocolate ao Leite", 3.99, "Doces"),
    ("Bala de Goma", 1.99, "Doces"),
    ("Salgadinho", 4.29, "Snacks"),
    ("Café Torrado", 8.99, "Bebidas"),
    ("Farinha de Trigo", 4.49, "Alimentos"),
    ("Maionese", 3.69, "Condimentos"),
    ("Ketchup", 4.29, "Condimentos"),
    ("Mostarda", 3.49, "Condimentos"),
    ("Pão de Forma", 6.49, "Padaria"),
    ("Margarina", 4.59, "Padaria")
]

cursor.executemany("INSERT INTO Produtos (nome, preco, categoria) VALUES (?, ?, ?);", produtos)


# ----------------------- #
# 3. Inserir 10 PEDIDOS   #
# ----------------------- #

# Pegando IDs disponíveis
cursor.execute("SELECT id FROM Clientes")
ids_clientes = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id, preco FROM Produtos")
produtos_disponiveis = cursor.fetchall()  # [(id, preco), ...]

for i in range(10):
    cliente_id = random.choice(ids_clientes)
    vendedor = f"Vendedor {i+1}"
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Inserir pedido
    cursor.execute("INSERT INTO Pedidos (data, vendedor, cliente_id) VALUES (?, ?, ?);", (data, vendedor, cliente_id))
    pedido_id = cursor.lastrowid

    # Adicionar de 2 a 5 itens ao pedido
    itens_pedido = random.sample(produtos_disponiveis, k=random.randint(2, 5))
    for produto_id, preco in itens_pedido:
        quantidade = random.randint(1, 5)
        cursor.execute("""
            INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, valor_unitario)
            VALUES (?, ?, ?, ?)
        """, (pedido_id, produto_id, quantidade, preco))


# ----------------------- #
# 4. Inserir via INPUT    #
# ----------------------- #

def inserir_cliente():
    nome = input("Nome do cliente: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO Clientes (nome, email, cidade, telefone) VALUES (?, ?, ?, ?);", (nome, email, cidade, telefone))

def inserir_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")
    cursor.execute("INSERT INTO Produtos (nome, preco, categoria) VALUES (?, ?, ?);", (nome, preco, categoria))

while True:
    opcao = input("\nDeseja inserir mais dados? (cliente/produto/não): ").strip().lower()
    if opcao == "cliente":
        inserir_cliente()
    elif opcao == "produto":
        inserir_produto()
    elif opcao in ["n", "não", "nao"]:
        break
    else:
        print("Opção inválida. Digite 'cliente', 'produto' ou 'não'.")

# ------------------------- #
# Finalizando e salvando    #
# ------------------------- #

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")
