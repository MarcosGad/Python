# in
# not in

# String
name = "Osama"
print("s" in name) # True
print("a" in name) # True
print("A" in name) # False


# List
friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends) # False
print("Sayed" in friends) # True
print("Mahmoud" not in friends) # False


# Using In and Not In With Condition
countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne:

  print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:

  print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:

  print("You Have No Discount")

# Hello You Have A Discount Equal To $50