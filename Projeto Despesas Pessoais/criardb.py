#https://www.youtube.com/watch?v=4n39KjF5k80&list=PLpm39GXipksInAqfxknE45I1y1pL9OozN&index=2
# Video 02
import sqlite3 as lite

#criando a conexão
con = lite.connect('dados.db')

#criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTERGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


#criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTERGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionando_em DATE, valor DECIMAL)")



#criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTERGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

#video 03    