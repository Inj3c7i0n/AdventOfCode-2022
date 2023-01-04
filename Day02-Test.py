# Read data from a file and strip all whitespace characters and put them in a list of strings.
# Then, print the list.
#

# Open the file.
with open("Day02-Example.in", "r") as file:
    # Make a list out of each line and replace the whitespace characters with nothing. Then split the "\n" characters.
    data = [line.replace(" ", "").split("\n") for line in file.read().strip().split("\n\n")]

# Print the list.
print(data)
