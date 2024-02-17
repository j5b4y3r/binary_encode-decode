def encode(input_string):
    binary_string = ""
    for char in input_string:
        binary_char = bin(ord(char))[2:].zfill(8)  # Convert character to binary (8 bits) and remove '0b' prefix
        binary_string += binary_char
    return binary_string
