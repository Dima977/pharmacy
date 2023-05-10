import sqlite3

with sqlite3.connect("pharmacy.db") as db:
    cur = db.cursor()
    a = cur.execute("""select count(id_medicines) from medicines""").fetchall()
    b = cur.execute("""select title from medicines""").fetchall()
    c = cur.execute("""select image from medicines""").fetchall()
    d = cur.execute("""SELECT description FROM medicines""").fetchall()
    e = cur.execute("""SELECT quantity FROM medicines""").fetchall()
    price = cur.execute("""SELECT price FROM medicines""").fetchall()




