import sqlite3

dbpath = "test2.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)""")

conn.commit()

cur = conn.cursor()
cur.execute(
"INSERT INTO items(name, price)VALUES(?,?)",
    ("Orange", 5200))
conn.commit()

cur = conn.cursor()
data = [("Mango",7700), ("Kiwi",4000), ("Grape",8000),
        ("Peach", 9400),("Persimmon",7000),("Banana",4000)]
cur.executemany(
"INSERT INTO items(name, price)VALUES(?,?)",
    data)
conn.commit()

cur = conn.cursor()
price_range = (4000, 7000)
cur.execute("SELECT * FROM items WHERE price>=? AND price<=?",
            price_range)
fr_list = cur.fetchall()

for it in fr_list:
    print(it)
