import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute("INSERT INTO teste (nome, telefone) VALUES ('RK', '9999-9999')")


con.commit()
con.close()
