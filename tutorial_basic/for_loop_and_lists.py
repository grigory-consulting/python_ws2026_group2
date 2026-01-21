

for i in range(10):
    print(i) # standard print prints string object and newline at the end 

for i in range(10):
    print(i, end="") #

print()

for i in range(10):
    print(i, end=" | ") #

 
print()

for i in range(10,0,-2): # from ten to two in -2 steps
    print(i, end = " ")

print()

l1 = [1,2,3] # list is an ordered, mutable container for everything 
print(l1)
l2 = [1., 2, "3"] # float, int, string
print(l2)
l3 = [1., 2, "3" ,l2] # float, int, string and list 
print(l3)


fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)

print(fruit) # last element after the loop is done 

for each in fruits: 
    print(each)


## List comprehension 

numbers = list(range(1,101))
print(numbers)

squares = [x*x for x in numbers]
print(squares)

# classical for loop
squares = [] # creation of empty list
for x in numbers:
    squares.append(x*x) # append to the list end
print(squares)

# cumulative loop (do not do it like that, because more overhead due to the list creation)
squares = []
for x in numbers:
    squares = squares + [x*x] # list concatenation 
print(squares)

food = ["rice", "beans", "bread", "broccoli"]

food += ["pizza", "hotdog"]
print(food)

# Slices
print(food[0]) # first element
print(food[-1]) # last element
print(food[2:]) # from third element to the end
print(food[:2]) # from start to second element
print(food[2:5]) # from third element to fifth element
print(food[5:2:-1]) # from sixth element to forth element

# mutability
food[0] = "apple juice"
print(food)

# Exercise 
words = ["apple", "egg", "banana", "sky", "time", "cherry"]

# Calculate the average word length

total = 0
for word in words:
    total += len(word)
average = total / len(words)

print(average)

# Task 2

names = ["Anna", "Ben", "Alex", "Marie", "Andreas", "Lena"]

# Filter the list names, such that there are only names that start with the letter "A"

names_w_A = []
for name in names:
    if name.lower().startswith("a"):
        names_w_A.append(name)

print(names_w_A)

# Same but as list comprehension 
names_w_A = [name for name in names if name.lower().startswith("a")]

# Task 3

l1 = [1,2,2,2,3,4,5,5,5,5,6,6,6,6,7,7,7,2,2,2,2,2,1,1,1,1,6,6,6,6,7,7,7,9,9,9,9]

# remove the duplicates 

l2 = []

for num in l1:
    if num not in l2:
        l2.append(num)
print(l2)

l2 = []

for num in l1:
    if num in l2:
        continue # skip 
    l2.append(num)
print(l2)

l2 = list(set(l1)) # best way to remove duplicates, if you do not care
# about order 

print(l2)

# TODO we will visit this part later 

# Task 4
l3 = [3,6,7,5,3,5,8,2,1,9,4]

# Find all unique pairs such that their sum is equal to ten
# Result:
# [[3,7], [4,6], [2,8], [1,9]]

pairs = []
for x in l3:
    for y in l3:
        if x + y == 10:
            if x <= y:
                if (x,y) not in pairs:
                    pairs.append((x,y))
print(pairs)

# TODO visit this code later
