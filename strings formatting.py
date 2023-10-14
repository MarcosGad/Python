# https://pyformat.info/
# format same C
name = "Osama"
age = 36
rank = 10

print("My Name is: " + name) # My Name is: Osama
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error (can only concatenate str)

# %s => String
# %d => Number
# %f => Float
print("My Name is: %s" % "Osama") # My Name is: Osama
print("My Name is: %s" % name) # My Name is: Osama
print("My Name is: %s and My Age is: %d" % (name, age)) # My Name is: Osama and My Age is: 36
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank)) # My Name is: Osama and My Age is: 36 and My Rank is: 10.000000

n = "Osama"
l = "Python"
y = 10
print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y)) # My Name is Osama Iam Python Developer With 10 Years Exp

# Control Floating Point Number
myNumber = 10
print("My Number is: %d" % myNumber) # My Number is: 10
print("My Number is: %f" % myNumber) # My Number is: 10.000000
print("My Number is: %.2f" % myNumber) # My Number is: 10.00

# Truncate String
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString) # Message is Hello Peoples of Elzero Web School I Love You All
print("Message is %.5s" % myLongString) # Message is Hello

# -- Strings Formatting New Ways --
# {:s} => String
# {:d} => Number
# {:f} => Float
print("My Name is: {}".format("Osama")) # My Name is: Osama
print("My Name is: {}".format(name)) # My Name is: Osama
print("My Name is: {} My Age: {}".format(name, age)) # My Name is: Osama My Age: 36
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank)) # My Name is: Osama Age: 36 & Rank is: 10.000000

n = "Osama"
l = "Python"
y = 10
print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y)) # My Name is Osama Iam Python Developer With 10 Years Exp

# Control Floating Point Number
myNumber = 10
print("My Number is: {:d}".format(myNumber)) # My Number is: 10
print("My Number is: {:f}".format(myNumber)) # My Number is: 10.000000
print("My Number is: {:.2f}".format(myNumber)) # My Number is: 10.00

# Truncate String
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString)) # Message is Hello Peoples of Elzero Web School I Love You All
print("Message is {:.5s}".format(myLongString)) # Message is Hello
print("Message is {:.13s}".format(myLongString)) # Message is Hello Peoples

# Format Money
myMoney = 500162350198
print("My Money in Bank Is: {:d}".format(myMoney)) # My Money in Bank Is: 500162350198
print("My Money in Bank Is: {:_d}".format(myMoney)) # My Money in Bank Is: 500_162_350_198
print("My Money in Bank Is: {:,d}".format(myMoney)) # My Money in Bank Is: 500,162,350,198

# ReArrange Items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z)) # Hello 20 30 10
print("Hello {2:f} {0:f} {1:f}".format(x, y, z)) # Hello 30.000000 10.000000 20.000000
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z)) # Hello 30.00 10.0000 20.00000

# Format in Version 3.6+
myName = "Osama"
myAge = 36
print("My Name is : {myName} and My Age is : {myAge}") # My Name is : {myName} and My Age is : {myAge}
print(f"My Name is : {myName} and My Age is : {myAge}") # My Name is : Osama and My Age is : 36