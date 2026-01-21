

print("Hello world!")


my_string1 = "hello"
my_string2 = "WorlD"

print(my_string1 + " " + my_string2 + "!") # string concatenation / merging

print(len(my_string2)) # length of the string -> integer = number of characters in the string
print('The string ' + '"' + my_string2 + '"' + " has " + str(len(my_string2)) + " characters.")
# str -> type conversion to the string

"""
Multiline comment
print(len(my_string2)) # length of the string -> integer = number of characters in the string
print('The string ' + '"' + my_string2 + '"' + " has " + str(len(my_string2)) + " characters.")
"""

# Accessing 
print(my_string1[0]) # first element
print(my_string1[1]) # second element
print(my_string1[-1]) # last element -> Python feature 
print(my_string1[-2]) # before last element 


print(my_string2.upper()) # everything uppercase
print(my_string2.lower()) # everything lowercase

print(my_string2.startswith("Wo"))
print(my_string2.startswith("wo"))
# better
print(my_string2.lower().startswith("wo"))
s = "Wo"
print(my_string2.lower().startswith(s.lower())) # pipelines

### 

var1 = "6"
var2 = "7"

print(var1 + var2)

print(int(var1) + int(var2)) # convert to integer

# floats

x = 6. # 6.0 
y = 7.2 
z = .8 # 0.8

print(float(var1) + float(var2)) # float to string

# https://docs.python.org/3/tutorial/floatingpoint.html

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
product = a*b

print(f"The product of {a} and {b} is equal to {product}.")

