import sqlite3 as lite

#criando a conexão
con = lite.connect('dados.db')

#Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query,i)


inserir_categoria(["Alimentacao"])

