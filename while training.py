myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]
print(len(myF))  # List Length (10)
print(myF[0]) # Os
print(myF[1]) # Ah

a = 0
while a < len(myF):  # a < 10
  print(f"#{str(a + 1).zfill(3)} {myF[a]}") # a + 1 start from 1
  a += 1
else: # when finsh
  print("All Friends Printed To Screen.")

#######################################################################################################

myFavouriteWebs = []
maximumWebs = 5

while maximumWebs > 0:

  # Input The New Website
  web = input("Website Name Without https:// ")
  myFavouriteWebs.append(f"https://{web.strip().lower()}")

  maximumWebs -= 1  # maximumWebs = maximumWebs - 1 (from 5)

  # Print The Add Message
  print(f"Website Added, {maximumWebs} Places Left")
  # Print The List
  print(myFavouriteWebs)

else:
  print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:
  # Sort The List
  myFavouriteWebs.sort()
  index = 0
  print("Printing The List Of Websites in Your Bookmark")

  while index < len(myFavouriteWebs):
    print(myFavouriteWebs[index])
    index += 1  # index = index + 1

#######################################################################################################

tries = 4
mainPassword = "Osama@123"
inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1 (atr7a)

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break # stop loop

    print("Will Not Print")

else: # tb3a while when be false
  print("Correct Password")