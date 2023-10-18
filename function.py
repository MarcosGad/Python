# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps

def function_name():
  print("Hello Python From Inside Function")
function_name() # Hello Python From Inside Function

def function_name():
  return "Hello Python From Inside Function"
dataFromFunction = function_name()
print(dataFromFunction) # Hello Python From Inside Function


# -- Function Parameters And Arguments --

a, b, c = "Osama", "Ahmed", "Sayed"
print(f"Hello {a}") # Hello Osama
print(f"Hello {b}") # Hello Ahmed
print(f"Hello {c}") # Hello Sayed

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name -> (n)             => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

def say_hello(n):
  print(f"Hello {n}")
say_hello(a) # Hello Osama
say_hello(b) # Hello Ahmed
say_hello(c) # Hello Sayed

def addition(n1, n2):
  print(n1 + n2)
addition(100, 300) # 400
addition(-50, 100) # 50

def addition(n1, n2):

  if type(n1) != int or type(n2) != int:
    print("Only Integers Allowed")
  else:
    print(n1 + n2)

addition(100, 500) # 600

def full_name(first, middle, last):
  print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("osama   ", 'mohamed', "elsayed") # Hello Osama M Elsayed


# -- Function Packing, Unpacking Arguments *Args --

myList = [1, 2, 3, 5]
print(myList) # [1, 2, 3, 5]
print(*myList) # 1 2 3 5

def say_hello(*peoples):  # n1, n2, n3, n4
  for name in peoples:
    print(f"Hello {name}")
say_hello("Osama", "Ahmed", "Sayed", "Mahmoud") # Hello Osama Hello Ahmed Hello Sayed Hello Mahmoud

def show_details(name, *skills):
  print(f"Hello {name} Your Skills Is: ")

  for skill in skills:
    print(skill)

show_details("Osama", "Html", "CSS", "JS") 
 # Hello Osama Your Skills Is: 
 # Html
 # CSS 
 # JS
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")


# -- Function Default Parameters --

def say_hello(name="Unknown", age="Unknown", country="Unknown"):
  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Osama", 36, "Egypt") # Hello Osama Your Age is 36 and Your Country Is Egypt
say_hello("Sameh", 38) # Hello Sameh Your Age is 38 and Your Country Is Unknown
say_hello("Ramy") # Hello Ramy Your Age is Unknown and Your Country Is Unknown
say_hello() # Hello Unknown Your Age is Unknown and Your Country Is Unknown


# -- Function Packing, Unpacking Arguments **KWArgs --

def show_skills_old(*skills):
  print(type(skills)) # <class 'tuple'>
  for skill in skills:
    print(f"{skill}")

show_skills_old("Html", "CSS", "JS") # Html CSS JS


mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):
  print(type(skills)) # <class 'dict'>
  for skill, value in skills.items():
    print(f"{skill} => {value}")

show_skills(**mySkills) # fka al3nasr (**) 

# -- Function Packing, Unpacking Arguments Trainings --

myTuple = ("Html", "CSS", "JS")
mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def show_skills(name, *myTuples, **skillsWithProgres):
  print(f"Hello {name} \nSkills Without Progress Is: ")
  for skill in myTuples:

    print(f"- {skill}")

  print("Skills With Progress Is: ")
  for skill_key, skill_value in skillsWithProgres.items():

    print(f"- {skill_key} => {skill_value}")

show_skills("Osama", *myTuple, **mySkills)
# Hello Osama
# Skills Without Progress Is:
# - Html
# - CSS
# - JS
# Skills With Progress Is:
# - Go => 80%
# - Python => 50%
# - MySQL => 80%