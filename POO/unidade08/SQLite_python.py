import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute("CREATE TABLE teste (nome TEXT, telefone TEXT)")


con.commit()
con.close()
