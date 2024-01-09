#https://www.youtube.com/watch?v=4n39KjF5k80&list=PLpm39GXipksInAqfxknE45I1y1pL9OozN&index=2

import sqlite3 as lite

#criando a conexão
con = lite.connect('dados.db')

#criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute()