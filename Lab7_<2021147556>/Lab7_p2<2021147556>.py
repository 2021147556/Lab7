alphabet_counts = {}
file_name = 'input_7_2.txt'

# Open the file
with open(file_name, 'r') as file:
    # Read the file
    content = file.read()
    # Loop each character
    for char in content:
        # If the character is an alphabet
        if char.isalpha():
            # Convert character to uppercase
            char = char.upper()
            # Increment the count for the alphabet
            if char in alphabet_counts:
                alphabet_counts[char] += 1
            else:
                alphabet_counts[char] = 1

    # Sort the alphabets based on their count
    sorted_alphabets = list(alphabet_counts.keys())
    sorted_alphabets.sort(key=lambda x: alphabet_counts[x], reverse=True)

    # Print
    print(sorted_alphabets)
