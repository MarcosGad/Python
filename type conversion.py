# str()
a = 10
print(type(a)) # <class 'int'>
print(type(str(a))) # <class 'str'>

# tuple()
c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary
print(tuple(c)) # ('O', 's', 'a', 'm', 'a')
print(tuple(d)) # (1, 2, 3, 4, 5)
print(tuple(e)) # ('C', 'A', 'B')
print(tuple(f)) # ('A', 'B')

# list()
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary
print(list(c)) # ['O', 's', 'a', 'm', 'a']
print(list(d)) # [1, 2, 3, 4, 5]
print(list(e)) # ['A', 'C', 'B']
print(list(f)) # ['A', 'B']

# set()
c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary
print(set(c)) # {'a', 'm', 'O', 's'} (not order)
print(set(d)) # {1, 2, 3, 4, 5}
print(set(e)) # {'A', 'B', 'C'}
print(set(f)) # {'A', 'B'}

# dict() (if found key and value)
d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List
print(dict(d)) # {'A': 1, 'B': 2, 'C': 3}
print(dict(e)) # {'One': 1, 'Two': 2, 'Three': 3}

