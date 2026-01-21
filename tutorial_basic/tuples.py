

x = (1,2,3)

# x[0] = 99 

l1 = ["a", "b", "c"]

x = (l1,)

# Problem: lists are mutable

l1[0] = "D"
print(x)

# it is questionable to put mutable types into immutable collections
