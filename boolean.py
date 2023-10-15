# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.

name = " "
print(name.isspace()) # True
print(100 > 200) # False
print(100 > 100) # False
print(100 > 90) # True

# True Values
print(bool("Osama")) # True
print(bool(100)) # True
print(bool(100.95)) # True
print(bool(True)) # True
print(bool([1, 2, 3, 4, 5])) # True

# False Values
print(bool(0)) # False
print(bool("")) # False
print(bool('')) # False
print(bool([])) # False
print(bool(False)) # False
print(bool(())) # False
print(bool({})) # False
print(bool(None)) # False

# and
# or
# not

age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False