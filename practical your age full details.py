# Input Age int(age type -> string)
age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:') # You Lived For:
print(f"{months} Months.") # 384 Months.
print(f"{weeks:,} Weeks.") # 1,536 Weeks.
print(f"{days:,} Days.") # 11,680 Days.
print(f"{hours:,} Hours.")# 280,320 Hours.
print(f"{minutes:,} Minutes.") # 6,819,200 Minutes.
print(f"{seconds:,} Seconds.") # 1,009,152,000 Seconds.