# Open the input file
with open("Day04.in") as file:
    # Initialize the running total to 0
    data = [i for i in file.read().strip().split("\n")]

# Initializing the variable `pairs` to 0.
pairs = 0

# Splitting the data into two parts, the first and second.
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]
    
    # Checking if the first range is completely inside the second range.
    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1
    
print("Answer to part 1:", pairs)

# Resetting the variable `pairs` to 0.
pairs = 0

# Splitting the data into two parts, the first and second.
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]
    
    
   # Checking if the the ranges overlap with each other.
    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs += 1
                        
print("Answer to part 2:", pairs)