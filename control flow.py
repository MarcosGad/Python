# -- If, Elif, Else --
# -- Make Decisions --

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

# -- Nested If --

uName = "Osama"
isStudent = "Yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

  if isStudent == "Yes":

    print(f"Hi {uName} Because U R From {uCountry} And Student")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

  else:

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


elif uCountry == "Kuwait" or uCountry == "Bahrain":

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")