#
# aska liye jo funcationaai ga wo hoga json.load
# wo jika type ka data hoga wo de dega
#

import json

d='{ "cname":"python","fees":12000,"duration":"2 month"}'

x=json.loads(d)
print(type(x))
print(x)

print()
## atrate

for a in x:
    print(a,x[a])