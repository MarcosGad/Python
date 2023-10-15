# append()
myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]
myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends) # append as one element
print(myFriends) # ['Osama', 'Ahmed', 'Sayed', 'Alaa', 100, 150.2, True, ['Haytham', 'Samah', 'Ali']]
print(myFriends[2]) # Sayed
print(myFriends[6]) # True
print(myFriends[7]) # ['Haytham', 'Samah', 'Ali']
print(myFriends[7][2]) # Ali

# extend()
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]
a.extend(b)
a.extend(c)
print(a) # [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two']

# remove()
x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x) # [1, 2, 3, 4, 5, True, 'Osama', 'Osama']

# sort()
y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y) # [120, 100, 29, 17, 2, 1, -10]

# reverse() بيعكس مش بيرتب زى السابقة
z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z) # [100, 'Osama', 100, 80, 9, 1, 10]

# clear()
a = [1, 2, 3, 4]
a.clear()
print(a) # []

# copy()
b = [1, 2, 3, 4]
c = b.copy()
print(b)  # Main List [1, 2, 3, 4]
print(c)  # Copied List [1, 2, 3, 4]
b.append(5)
print(b)  # Main List [1, 2, 3, 4, 5]
print(c)  # Copied List [1, 2, 3, 4]

# count()
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1)) # 3

# index()
e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy")) # 3

# insert()
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f) # ['Test', 1, 2, 3, 4, 5, 'A', 'Test', 'B']

# pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3)) # 5