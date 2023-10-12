## update matlb  apka ka passs pehle sy he record parah hai osme apko kuch cahnge krna hai

import sqlite3
conn=sqlite3.connect("sqlite.db")

conn.execute('''
    update student set st_name="ram1",st_class='10th' where st_id=1

''')

conn.commit()
conn.commit()