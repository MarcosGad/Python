# type()
# All Data in Python is Object

print(type(10))  # int => Integer <class 'int'>
print(type(100))  # int => Integer <class 'int'> 
print(type(-50))  # int => Integer <class 'int'> 
 
print(type(100.9))  # float => Floating Point Number <class 'float'>
print(type(1.950950))  # float => Floating Point Number <class 'float'>
print(type(-100.9595))  # float => Floating Point Number <class 'float'>

print(type("Hello Python"))  # str => String <class 'str'> 

print(type([1, 2, 3, 4, 5]))  # list => List <class 'list'>
print(type((1, 2, 3, 4, 5)))  # tuple => Tuple <class 'tuple'>

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary <class 'dict'>

print(type(2 == 2))  # bool => Boolean <class 'bool'>