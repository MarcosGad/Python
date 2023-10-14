a = " I Love Python"
print(len(a)) #14

# strip() rstrip() lstrip()
a = "    I Love Python    "
print(a.strip()) # I Love Python
print(a.rstrip()) #     I Love Python
print(a.lstrip()) # I Love Python
a = "#####I Love Python####"
print(a.strip("#")) # I Love Python
print(a.rstrip("#")) # #####I Love Python
print(a.lstrip("#")) # I Love Python####
a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#")) # I Love Python
print(a.rstrip("@#")) # @#@#@#I Love Python
print(a.lstrip("@#")) # I Love Python@#@#@#

# title()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title()) # I Love 2D Graphics And 3G Technology And Python

# capitalize()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize()) # I love 2d graphics and 3g technology and python

# zfill
c, d, e, f = "1", "11", "111", "1111"
print(c) # 1
print(d) # 11
print(e) # 111
print(f) # 1111
print(c.zfill(4)) # 0001
print(d.zfill(4)) # 0011
print(e.zfill(4)) # 0111
print(f.zfill(4)) # 1111

# upper()
g = "osama"
print(g.upper()) # OSAMA

# lower()
h = "OSama"
print(h.lower()) # osama

# split() rsplit()
a = "I Love Python and PHP and MySQL"
print(a.split()) # ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']
b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-")) # ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']
c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3)) # ['I', 'Love', 'Python', 'and-PHP-and-MySQL']
d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3)) # ['I-Love-Python-and', 'PHP', 'and', 'MySQL']

# center()
e = "Osama"
print(e.center(9))  # Spaces (  Osama)
print(e.center(9, "#"))  # Hashes (##Osama##)
print(e.center(15, "@"))  # @ (@@@@@Osama@@@@@)

# count()
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words (2)
print(f.count("PHP", 0, 25))  # Only One PHP Word (1)

# swapcase()
g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase()) # i lOVE pYTHON
print(h.swapcase()) # I Love Python

# startswith()
i = "I Love Python"
print(i.startswith("I")) # True
print(i.startswith("S")) # False
print(i.startswith("P", 7, 12)) # True

# endswith()
j = "I Love Python"
print(j.endswith("n")) # True
print(j.endswith("S")) # False
print(j.endswith("e", 2, 6)) # True

# index(SubString, Start, End)
a = "I Love Python"
print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error ( substring not found )

# find(SubString, Start, End)
b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)
c = "Osama"
print(c.rjust(10)) #     Osama
print(c.rjust(10, "#")) # #####Osama
d = "Osama"
print(d.ljust(10)) # Osama
print(d.ljust(10, "#")) # Osama#####

# splitlines()
e = """First Line
Second Line
Third Line"""
print(e.splitlines()) # ['First Line', 'Second Line', 'Third Line']
f = "First Line\nSecond Line\nThird Line"
print(f.splitlines()) # ['First Line', 'Second Line', 'Third Line']

# expandtabs() number of tab
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2)) # Hello World I Love  Python

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # True
print(two.istitle()) # False

three = " "
four = ""
print(three.isspace()) # True
print(four.isspace()) # False

five = 'i love python'
six = 'I Love Python'
print(five.islower()) # True
print(six.islower()) # False

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"
print(seven.isidentifier()) # True good for variable
print(eight.isidentifier()) # True
print(nine.isidentifier()) # False

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha()) # True
print(y.isalpha()) # False

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum()) # True alpha and number
print(z.isalnum()) # True

# replace(Old Value, New Value, Count)
a = "Hello One Two Three One One"
print(a.replace("One", "1")) # Hello 1 Two Three 1 1
print(a.replace("One", "1", 1)) # Hello 1 Two Three One One
print(a.replace("One", "1", 2) )# Hello 1 Two Three 1 One

# join(Iterable)
myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList)) # Osama-Mohamed-Elsayed
print(" ".join(myList)) # Osama Mohamed Elsayed
print(", ".join(myList)) # Osama, Mohamed, Elsayed
print(type(", ".join(myList))) # <class 'str'>