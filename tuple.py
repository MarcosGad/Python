# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples


myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"
print(myAwesomeTupleOne) # ('Osama', 'Ahmed')
print(myAwesomeTupleTwo) # ('Osama', 'Ahmed')
print(type(myAwesomeTupleOne)) # <class 'tuple'>
print(type(myAwesomeTupleTwo)) # <class 'tuple'>

# Tuple Indexing
myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0]) # 1
print(myAwesomeTupleThree[-1]) # 5 
print(myAwesomeTupleThree[-3]) # 3

# Tuple Assign Values ( dont edit ) 
myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data
myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1]) # Osama
print(myAwesomeTupleFive[-1]) # True

# Tuple With One Element must add(,)
myTuple1 = ("Osama",)
myTupleS = ("Osama")
myTuple2 = "Osama",
print(myTuple1) # ('Osama',)
print(myTuple2) # ('Osama',)
print(type(myTuple1)) # <class 'tuple'>
print(type(myTupleS)) # <class 'str'>
print(type(myTuple2)) # <class 'tuple'>
print(len(myTuple1)) # 1
print(len(myTuple2)) # 1

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
d = a + ("A", "B", True) + b
print(c) # (1, 2, 3, 4, 5, 6)
print(d) # (1, 2, 3, 4, 'A', 'B', True, 5, 6)

# Tuple, List, String Repeat (*)
myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")
print(myString * 6) # OsamaOsamaOsamaOsamaOsamaOsama
print(myList * 6) # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 6) # ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')

# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8)) # 2

# Methods => index()
b = (1, 3, 7, 8, 2, 6, 5)
print(b.index(7)) # 2
# print("The Position of Index Is: " + b.index(7))  # Error can only concatenate str + int
print("The Position of Index Is: {:d}".format(b.index(7))) # The Position of Index Is: 2
print(f"The Position of Index Is: {b.index(7)}") # The Position of Index Is: 2

# Tuple Destruct (_)
a = ("A", "B", 4, "C")
x, y, _, z = a
print(x) # A
print(y) # B
print(z) # C