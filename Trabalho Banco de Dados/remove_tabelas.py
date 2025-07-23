import sqlite3
from datetime import datetime
import random

# Conectar ao banco de dados
conexao = sqlite3.connect("SuperMercado_SupriBem.db")
cursor = conexao.cursor()
cursor.execute('DROP TABLE IF EXISTS Clientes')
cursor.execute('DROP TABLE IF EXISTS ItensPedido')
cursor.execute('DROP TABLE IF EXISTS Pedidos')
cursor.execute('DROP TABLE IF EXISTS Produtos')
