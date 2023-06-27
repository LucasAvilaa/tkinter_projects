import sqlite3 as lite

con = lite.connect("travel.db")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Quantia(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL)")
    cur.execute("CREATE TABLE Despesa(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, descricao TEXT, valor DECIMAL)")