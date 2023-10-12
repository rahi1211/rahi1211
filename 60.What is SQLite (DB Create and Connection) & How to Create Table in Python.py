import sqlite3

conn = sqlite3.connect("sqlite.db")
conn.execute('''
    CREATE TABLE student (
        st_id INTEGER PRIMARY KEY,
        st_name VARCHAR(50),
        st_Class VARCHAR(10),
        st_Email VARCHAR(30)
    )
''')

conn.close()
