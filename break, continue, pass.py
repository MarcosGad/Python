myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue
for number in myNumbers:
  if number == 13:

    continue

  print(number) # all but remove 13


# Break
for number in myNumbers:
  if number == 13:

    break

  print(number) # when show 13 stop


# Pass
for number in myNumbers:

  if number == 13:

    pass # 3dyhaaa 7ta lo error

  print(number)