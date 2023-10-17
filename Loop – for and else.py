myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:
  
  # print(number)

  if number % 2 == 0:  # Even
    print(f"The Number {number} Is Even.")
  else:
    print(f"The Number {number} Is Odd.")

else:
  print("The Loop Is Finished")

myName = "Osama"
for letter in myName:
  print(f" [ {letter.upper()} ] ") #  [ O ] [ S ] [ A ] [ M ] [ A ]

#######################################################################################################

# Range
myRange = range(1, 101)

for number in myRange:

  print(number) # 1 -> 100


# Dictionary
mySkills = {
  "Html": "90%",
  "Css": "60%",
  "PHP": "70%",
  "JS": "80%",
  "Python": "90%",
  "MySQL": "60%"
}

print(mySkills['JS']) # 80%
print(mySkills.get("Python")) # 90%

for skill in mySkills:

  # print(skill)

  print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}") # My Progress in Lang Html Is: 90%

#######################################################################################################
# -- Nested Loop --

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop
  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop
    print(f"- {skill}")

# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

print(peoples["Osama"]) # {'Html': '70%', 'Css': '80%', 'Js': '70%'}
print(peoples["Ahmed"]) # {'Html': '90%', 'Css': '80%', 'Js': '90%'}
print(peoples["Sayed"]) # {'Html': '70%', 'Css': '60%', 'Js': '90%'}

print(peoples["Osama"]['Css']) # 80%
print(peoples["Ahmed"]['Css']) # 80%
print(peoples["Sayed"]['Css']) # 60%

for name in peoples:
  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]:
    print(f"{skill.upper()} => {peoples[name][skill]}")