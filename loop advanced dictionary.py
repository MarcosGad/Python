mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}
print(mySkills.items()) # dict_items([('HTML', '80%'), ('CSS', '90%'), ('JS', '70%'), ('PHP', '80%')])

for skill in mySkills:
  print(f"{skill} => {mySkills[skill]}") # HTML => 80%

for skill_key, skill_progress in mySkills.items():
  print(f"{skill_key} => {skill_progress}") # HTML => 80%


myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():
  print(f"{main_key} Progress Is: ") # HTML Progress Is:

  for child_key, child_value in main_value.items():
    print(f"- {child_key} => {child_value}") # - Main => 80% 
                                             # - Pugjs => 80% 