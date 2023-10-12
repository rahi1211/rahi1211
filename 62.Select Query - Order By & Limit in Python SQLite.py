## seclct query sy ap apni data comand py show karea stke ho

import sqlite3

conn = sqlite3.connect("sqlite.db")

data=conn.execute("SELECT * FROM student lIMIT 1,2")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENY EMAIL")
for n in data:
    print(n[0],"   ",n[1],"   ",n[2],n[3])



## AB DATA TUPLE ME AA GYA HAI TOH AP OSKE PARAMATER OR FUNCATIONS OS PY LAGA SKTE HO

print()

## LIMIT IN SQLITE

## APKO LIMITED F=DATA CHAIYE UPAR KUCH NICHE KUCH ASA
## JAHA PY SEXLRCT QUERY HAI WAHA HOGA
## AGR APNA 0,2 KIYE TO 1,2 DIKAO GA
## AND 2,2 KIYE TOH 3,AND 4 DIKAI GA