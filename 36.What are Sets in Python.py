# a set is collection which is unorderd and unindexed that is iterable
# mutable and has no duplicate elements
# {}

s={12,32,45,65,99,555,666,777,123}
print(s)
print(type(s))


## irrate
print()

for a in s:
    print(a)


## sets fuvations:-

##1 sets: agr apke pass koi list ya str hai to yeh osko set me convt kr dega

##2 remove: remove kar dega set andr ki value ki but agr wo value ahr andr nhi howe toh ye aoko error de dega

##3 discard: aska kaam be hota remove krna but agr koi vakue andr nhi howe to ye error nhi dega

##4 pop:pop be remove kerta hai but koi random kuch be rm kr dega
## agr ap pop ko print be kro ge to wo apko bata be dega ki osne kia del kiye hai

##5 clear: pure tarah sy set ko clear kr dega

##6 add: koi value ad krni ka kaam ata hai

## update:koi list ap update krna cate ho jo pane howe ha

print()

l=[100,200,300,500,123]
r=set(l)
print(r)

print()

s.remove(12)
print(s)

print()

s.discard(65)
print(s)

print()

print(s.pop())


print()


s.clear()
print(s)

print()

s.add(123)
print(s)

print()

s.update(l)
print(s)
