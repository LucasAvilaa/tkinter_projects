import sqlite3 as lite

con = lite.connect("travel.db")


""" GET """
def get_orcamento():
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Quantia")
        row = cur.fetchone()
        return row[0] or 0

def get_all_despesa():
    list_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesa")

        row = cur.fetchall()

        list_itens = [r for r in row]

    return list_itens

def get_all_values_despesa():
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Despesa")

        row = cur.fetchall()

        return [r[0] for r in row]

def get_categories():
    with con:
        cur = con.cursor()
        cur.execute("SELECT distinct(categoria) FROM Despesa")

        row = cur.fetchall()
        return [x[0] for x in row]

def get_values_graph():
    with con:
        cur = con.cursor()
        cur.execute("SELECT sum(valor) FROM Despesa GROUP BY categoria")

        row = cur.fetchall()
        return [x[0] for x in row]

""" Update """

def update_despesa_db(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Despesa SET categoria = ?, descricao = ?, valor = ? WHERE ID = ?"
        cur.execute(query, i)


""" Insert """

def insert_despesa(i):
    with con: 
        cur = con.cursor()

        query = "INSERT INTO Despesa (categoria, descricao, valor) VALUES (?,?,?)"
        cur.execute(query, i)

def insert_total_orcamento(i):
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Quantia")
        cur.execute("INSERT INTO Quantia (valor) VALUES (?)", i)
    
    
""" Delete """

def delete_despesa_db(i):
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Despesa WHERE ID= ?", i)

""" Function Sum """

def get_total_despesa():
    with con:
        cur = con.cursor()
        cur.execute("SELECT sum(valor) FROM Despesa")

        row = cur.fetchone()
    return row[0] or 0

def sum_by_category(i):
    with con:
        cur = con.cursor()
        cur.execute("SELECT valor FROM Despesa WHERE categoria = ?", i)

        row = cur.fetchall()

        total = 0
        for l in row:
            value = l[0]
            if type(value) == str:
                value = float(value.replace(",","."))
            total += value
        return total