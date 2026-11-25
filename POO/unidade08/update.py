import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute("UPDATE teste SET telefone= '988001977' WHERE nome = 'Alexandre'")

con.commit()
con.close()

