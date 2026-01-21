

def cube(num):
    cube_num = num**3
    return cube_num

num1 = 5
num2 = 6 

print(cube(num1))
print(cube(num2))

def mysum(*args):
    total = 0
    print(args)
    for i in args:
        #print(i)
        total += i
    return total

print(mysum(1,2,48,293,49))

def print_key_vals(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_vals(arg1 = "1", arg2 = 2, arg3 = [1,2,3], arg4 = {1,2,3,4} )


def add_three_numbers(a,b,c=1):
    print("a =", a, "b =", b, "c =", c )
    return a+b+c
#def add_three_numbers(a=1,b,c):
#    print("a =", a, "b =", b, "c =", c )
#    return a+b+c


print(add_three_numbers(1,2))
print(add_three_numbers(2,1))
print(add_three_numbers(1,2,3)) 
print(add_three_numbers(c=4,b=2,a=10)) # accessing by name
print(add_three_numbers(10,c = 2, b=4)) 
# print(add_three_numbers(c=2,10,b=1)) doesnt work


def everything(a, b=1, *args, **kwargs):
    print("a", a)
    print("b", b)
    print("args", args)
    print("kwargs", kwargs)

everything(3,70,4,5,3,Name="Anna", Street="Street", y = [])