# https://www.javatpoint.com/escape-sequences-in-python
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value (https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/)

# Back Space
print("Hello\bWorld")  # Will Remove o ( HellWorld )

# Escape New Line + Back Slash ( Hello I Love Python )
print("Hello \
I Love \
Python")

# Escape Back Slash ( I Love Back Slash \ )
print("I Love Back Slash \\")

# Escape Single Quote ( I Love Single Quote 'Test' )
print('I Love Single Quote \'Test\' ')

# Escape Double Quotes ( I Love Double Quotes "Test" )
print("I Love Double Quotes \"Test\" ")

# Line Feed
# Hello World
# Second Line
print("Hello World\nSecond Line")

# Carriage Return ( Abcde6 )
print("123456\rAbcde")

# Horizontal Tab ( Hello   Python )
print("Hello\tPython")

# Character Hex Value ( Os )
print("\x4F\x73")