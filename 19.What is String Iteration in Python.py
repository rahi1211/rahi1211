# iteration hum kehti hain jisa humre pass ek string hai hum osko ek ek word ko laka ana chata hon
# to ose hum iteration kehta hain

w = "wellcome to wscubetech"
# 1 option
# w=w[-1::-1]

t = len(w)

print(t)

print()

for a in range(t):
    print(w[a])

print()

for a in range(t - 1, -1, -1):
    print(w[a])

print()
# 2nd opation man option

w = "wellcome to wscubetrch"

for a in w:
    print(a)

# revharse in this
# asme apko string ko pehle sy he revarse krna padha ga


print()

w = "wellcome to wscubetech"
w = w[-1::-1]

print(w)

