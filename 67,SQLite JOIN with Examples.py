import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("sqlite.db")
print("STUDENT ID","STUDENT Name","STUDENT FEES")
data=conn.execute("SELECT f.st_id,s.st_name,f.fees_amount FROM fees as f full join student as s on f.st_id=s.st_id")
for a in data:
    print(a[0],a[1],a[2])
conn.close()

## agr * laga ka kro ge to pure data aa kiye ge on select

## ap asme joins ka use kren ge

## jions kon kon sa hoti hain

## 1 inner: inner 2  no table me jo jo data match kre ga wo apko mil jiye ga

## 2 left : left table ka sara data mil jiye ga
## or riht wahi aai ga jo match r raha ha


