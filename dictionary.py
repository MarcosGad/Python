# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key not index

user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user) # {'name': 'Osama', 'age': 36, 'country': 'Egypt', 'skills': ['Html', 'Css', 'JS'], 'rating': 10.5}
print(user['country']) # Egypt
print(user.get("country")) # Egypt
print(user.keys()) # dict_keys(['name', 'age', 'country', 'skills', 'rating'])
print(user.values()) # dict_values(['Osama', 36, 'Egypt', ['Html', 'Css', 'JS'], 10.5])

# Two-Dimensional Dictionary
languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages) # {'One': {'name': 'Html', 'progress': '80%'}, 'Two': {'name': 'Css', 'progress': '90%'}, 'Three': {'name': 'Js', 'progress': '90%'}}
print(languages['One']) # {'name': 'Html', 'progress': '80%'}
print(languages['Three']['name']) # Js

# Dictionary Length
print(len(languages)) # 3
print(len(languages["Two"])) # 2

# Create Dictionary From Variables
frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework) # {'one': {'name': 'Vuejs', 'progress': '80%'}, 'two': {'name': 'ReactJs', 'progress': '80%'}, 'three': {'name': 'Angular', 'progress': '80%'}}

# ----------------------------------- Dictionary Methods  -------------------------------------------

# clear()
user = {
  "name": "Osama"
}
print(user) # {'name': 'Osama'}
user.clear()
print(user) # {}

# update()
member = {
  "name": "Osama"
}
print(member) # {'name': 'Osama'}
member["age"] = 36
print(member) # {'name': 'Osama', 'age': 36}
member.update({"country": "Egypt"})
print(member) # {'name': 'Osama', 'age': 36, 'country': 'Egypt'}

# copy()
main = {
  "name": "Osama"
}
b = main.copy()
print(b) # {'name': 'Osama'}
main.update({"skills": "Fighting"})
print(main) # {'name': 'Osama', 'skills': 'Fighting'}
print(b) # {'name': 'Osama'}

# keys() + values()
print(main.keys()) # dict_keys(['name', 'skills'])
print(main.values()) # dict_values(['Osama', 'Fighting'])

# setdefault() get or update 
user = {
  "name": "Osama"
}
print(user) # {'name': 'Osama'}
print(user.setdefault("age", 36)) # 36
print(user) # {'name': 'Osama', 'age': 36}

# popitem() last element update 
member = {
  "name": "Osama",
  "skill": "PS4"
}
print(member) # {'name': 'Osama', 'skill': 'PS4'}
member.update({"age": 36}) 
print(member.popitem()) # ('age', 36)

# items()
view = {
  "name": "Osama",
  "skill": "XBox"
}
allItems = view.items()
print(view) # {'name': 'Osama', 'skill': 'XBox'}
view["age"] = 36
print(allItems) # dict_items([('name', 'Osama'), ('skill', 'XBox'), ('age', 36)])

# fromkeys()
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"
print(dict.fromkeys(a, b)) # {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'}