

# Dictionary

# mutable collection of key-value pairs
# key immutable, values anything 

d1 = {True: {1}, False: [2]}
d2 = {True: {1}, False: {2}}
d2 = {True: 1, False: 2}

# something that doesnt work:
# d = {[1,2]:3 }
d = {(1,2):3 }

d = {
    "one": 1,
    "two": [2],
    "three": "THREE",
    4: {"four": "FOUR"},
    (5,): [5.0, 5],
    6: 6,
}

# KeyError: 'six'
# print(d["six"])

print(d.get("six", "Key is not found!"))

del d["one"] # Remove key:value
val = d.pop("three")

print(d)
print(val)

# iterate

for key in d:
    print(key, d[key])

keys = list(d.keys()) # list of keys
values = list(d.values()) # list of values
items = list(d.items()) # list of Key-Value-Tuple
print(items)
  

# Task

colors = ["red", "red", "red", "blue", "yellow", "red", "brown", "blue"]

# Count with the help of dictionaries the occurences of each color 
# Result
# d_colors = {"red": 4, "blue": 2, ... }

# Hints
d_colors = {} # empty dict
#d_colors["red"] = 4 # update dictionary

for color in colors:
    if color in d_colors:
        d_colors[color] += 1
    else:
        d_colors[color] = 1
print(d_colors)

d_colors = {}

for color in colors:
    d_colors[color] = colors.count(color)

print(d_colors)

d_colors = {}
for color in colors:
    d_colors[color] = d_colors.get(color,0) +1

print(d_colors)

