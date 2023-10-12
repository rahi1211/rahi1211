import sqlite3

conn = sqlite3.connect("sqlite.db")

ins = '''
    INSERT INTO student (st_name, st_Class, st_Email) VALUES
    ('Ravi1', '12th', 'ravi1@gmail.com')
'''

conn.execute(ins)
conn.commit()
conn.close()
