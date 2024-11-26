import sqlite3
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS counts")
cur.execute('CREATE TABLE counts(email TEXT, count INTEGER)')
sqlStr = ("INSERT INTO counts(email, count) VALUES('yon@sql.com', 3)")
cur.execute(sqlStr)
sqlSelect = "SELECT * FROM counts"
conn.commit()
#iterate and print
# for row in cur.execute(sqlSelect):
    # print(row)
    # print(row[0],row[1])

# assignment 1
# cur.execute('''
#             CREATE TABLE Ages ( 
#     name VARCHAR(128), 
#     age INTEGER
#     )
# ''')
# conn.commit()
# cur.execute(
#     '''
#     INSERT INTO Ages (name, age) VALUES
#     ('Jaidyn', 38),
#     ('Harlie', 22),
#     ('Daood', 35),
#     ('Declan', 16);
#     '''
# )
# cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
# rows = cur.fetchall()
# for row in rows:
#     print(row)
conn.commit()
cur.close()

