myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"
print(myStringOne) # This is Single Quote
print(myStringTwo) # This is Double Quotes

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"
print(myStringThree) # This is Single Quote "Test"
print(myStringFour) # This is Double Quotes 'Test'


# ''' more lines ''' """ more lines """
myStringFive = '''First
Second 'Test' "Test"
Third'''
myStringSix = """First
Second "Test" \\\ 'Test'
Third"""
print(myStringFive)
print(myStringSix) 

############################################################################################

# Indexing ( Access Single Item )
myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t
print(myString[-1])  # Index -1 => First Character From End -> n
print(myString[-6])  # Index -6 => 6th Character From End -> P


# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data
print(myString[::2]) # ILv yhn
print(myString[::3]) # Io tn






