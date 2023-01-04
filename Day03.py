# Create a dictionary to store the values of each letter
letter_values = {
    "a": 1, "b": 2, "c": 3, "d": 4,  "e": 5, "f": 6, "g": 7,
    "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
    "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28,
    "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
    "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40,
    "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
    "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
}

# Open the input file
with open("Day03-Example.in", "r") as file:
    # Initialize the running total to 0
    total = 0

# For each line in the file
    for line in file:
        # Split the input string in half
        half1 = line[:len(line) // 2]
        half2 = line[len(line) // 2:]
        print(half1, half2)

        # Sum the value of every letter that both halves have
        for letter in half1:
            if letter in half2:
                print(letter_values[letter])
                total += letter_values[letter]

# Print the total
print(total)
