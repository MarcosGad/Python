# -- Assignment Operators -- تعين 
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=

# Var One = Self [Operator] Var Two
# Var One [Operator]= Var Two
x = 10  # Var One
y = 20  # Var Two

x += y
# x -= y # -10
print(x) # 30


# -- Comparison Operators --
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal

# Equal + Not Equal
print(100 == 100) # True
print(100 == 200) # False
print(100 == 100.00) # False
print(100 != 100) # False
print(100 != 200) # True
print(100 != 100.00) # False

# Greater Than + Less Than
print(100 > 100) # False
print(100 > 200) # False
print(100 > 100.00) # False
print(100 > 40) # True
print(100 < 100) # False
print(100 < 200) # True
print(100 < 100.00) # False
print(100 < 40) # False

print("#" * 50)


# Greater Than Or Equal + Less Than Or Equal
print(100 >= 100) # True
print(100 >= 200) # False
print(100 >= 100.00) # True
print(100 >= 40) # True
print(100 <= 100) # True
print(100 <= 200) # True
print(100 <= 100.00) # True
print(100 <= 40) # False