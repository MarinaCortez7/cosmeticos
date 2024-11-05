import sqlite3
conexao=sqlite3.connect('Produtos.db')
cursor=conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
    ID INTEGER PRIMARY KEY,
    Nome TEXT,
    DataValidade TEXT,
    Marca TEXT,
    Categoria TEXT,
    Quantidade TEXT,
    Preço TEXT,
    Descrição TEXT,
    Tipo TEXT)
''')
conexao.close()

