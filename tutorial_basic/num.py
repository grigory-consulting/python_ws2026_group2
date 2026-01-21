total = 0
count = 0
print("0 to stop")
num = int(input("Enter a number: "))
while num != 0:
    total += num
    count += 1
    #print("0 to stop")
    num = int(input("Enter a number: "))
print("Count:", count)
print("Sum:", total)