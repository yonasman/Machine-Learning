import sqlite3
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS counts")
cur.execute('CREATE TABLE counts(email TEXT, count INTEGER)')
cur.execute("INSERT INTO counts(email, count) VALUES('yon@sql.com', 2)")




