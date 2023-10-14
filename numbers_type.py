# Integer <class 'int'>
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float <class 'float'>
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex
myComplexNumber = 5+6j 
print(type(myComplexNumber)) # <class 'complex'>
print("Real Part Is: {}".format(myComplexNumber.real)) # Real Part Is: 5.0
print("Imaginary Part Is: {}".format(myComplexNumber.imag)) # Imaginary Part Is: 6.0

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100) # 100
print(float(100)) # 100.0
print(complex(100)) # (100+0j)

print(10.50) # 10.5
print(int(10.50)) # 10
print(complex(10.50)) # (10.5+0j)

print(10+9j) # 10+9j)
print(int(10+9j)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'