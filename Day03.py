# # Create a dictionary to store the values of each letter
# letter_values = {
#     "a": 1, "b": 2, "c": 3, "d": 4,  "e": 5, "f": 6, "g": 7,
#     "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
#     "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
#     "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28,
#     "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
#     "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
#     "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
#     "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
# }

from string import ascii_letters

# Open the input file
with open("Day03.in", "r") as file:
    # Initialize the running total to 0
    data = [i for i in file.read().strip().split("\n")]
    
# ---===[PART ONE]===---
totalSum = 0
for line in data:
    # Make a halfway point
    half = len(line)//2
    
    # Split the input string in half
    half1 = set(line[:half])
    half2 = set(line[half:])
   
    # print(half1, half2)
    
    for value, character in enumerate(ascii_letters):
        if character in half1 and character in half2:
            totalSum += value + 1

# Print the total
print("Answer to Part 1:", totalSum)

# ---===[PART TWO]===---
totalSum = 0
# Iterate through the list in steps of 3
for i in range(0, len(data), 3):
  # Get the current group of 3 lines
  group = data[i:i+3]
  # print(group)
  # Check for common letters between the lines of the group
  common_letters = set(group[0]) & set(group[1]) & set(group[2])
  for value, character in enumerate(ascii_letters):
    if character in common_letters:
      totalSum += value + 1

      
print("Answer to Part 2:", totalSum)
