#!/usr/bin/python3

# Getting the input data
with open('Day01.in') as file:
    data = [i for i in file.read().strip().split("\n")]     # Put Data in a list seperated by empty strings.

# print(data)


max1 = 0    # Elf with highest calorie count
max2 = 0    # Elf with 2nd highest calorie count
max3 = 0    # Elf with 3nd highest calorie count
count = 0
# Traversing every STRING in our DATA file
for item in data:
    if item == '':
        count = 0       # Resetting count at empty string
    else:
        num = int(item)     # Turn (STR)ing into (INT)eger.
        count += num        # Adding the number to the count.

    # Find our max values and
    # shift the previous max value(s)
    # before setting new ones.
    if count > max1:
        max3 = max2
        max2 = max1
        max1 = count
    elif count > max2:
        max3 = max2
        max2 = count    # Elf with 2nd to most
    elif count > max3:
        max3 = count    # Elf with 3rd to most

print("Answer to part 1:", max1)
print("Answer to part 2:", max1+max2+max3)
