# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique

# Not Ordered And Not Indexed
mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne) # not order
# print(mySetOne[0]) # TypeError: 'set' object is not subscriptable  

# Slicing Cant Be Done
mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) # TypeError: 'set' object is not subscriptable

# Has Only Immutable Data Types (dont incloud type list)
# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}
print(mySetThree) # not order

# Items Is Unique
mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour) # {1, 2, 'Osama', 'One'}

# ----------------------- Set Methods -------------------------------------------

# clear()
a = {1, 2, 3}
a.clear()
print(a) # set()

# union() دمج العناصر مع بعض 
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}
print(b | c) 
print(b.union(c, x))

# add()
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d) # {1, 2, 3, 4, 5, 6}

# copy()
e = {1, 2, 3, 4}
f = e.copy()
print(e) # {1, 2, 3, 4}
print(f) # {1, 2, 3, 4}
e.add(6)
print(e) # {1, 2, 3, 4, 6}
print(f) # {1, 2, 3, 4}

# remove()
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7) # KeyError is not found (7)
print(g)  # {2, 3, 4}

# discard()
h = {1, 2, 3, 4}
h.discard(1) 
h.discard(7) # not error 7 not found
print(h) # {2, 3, 4}

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop()) # (random element)

# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)
print(j) 

# difference() القيم المختلفة
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a) # {1, 2, 3, 4}
print(a.difference(b))  # {4}
print(a) # {1, 2, 3, 4}

# difference_update()
c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c) # {1, 2, 3, 4}
c.difference_update(d)  # c - d
print(c) # {3, 4}

# intersection() القيم المتكررة
e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e) # {1, 2, 3, 4, "X", "Osama"}
print(e.intersection(f))  # e & f {'Osama', 2, 'X'}
print(e) # {1, 2, 3, 4, "X", "Osama"}

# intersection_update()
g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g) # {1, 2, 3, 4, "X", "Osama"}
g.intersection_update(h)  # g & h 
print(g) # {'Osama', 2, 'X'}

# symmetric_difference() القيم الغير موجود فى 2
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i) # {1, 2, 3, 4, 5, 'X'}
print(i.symmetric_difference(j))  # i ^ j {3, 5, 'Zero', 'Osama'}
print(i) # {1, 2, 3, 4, 5, 'X'}

# symmetric_difference_update()
k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}
print(k) # {1, 2, 3, 4, 5, 'X'}
k.symmetric_difference_update(l)  # k ^ l
print(k) # {3, 5, 'Osama', 'Zero'}

# issuperset() كل العناصر موجود أم لا
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

# issubset() عكس السابقة
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print(d.issubset(e))  # False
print(d.issubset(f))  # True

# isdisjoint() منفصلين عن بعض
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}
print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True