def decode(binary_string):
    decoded_string = ""
    for i in range(0, len(binary_string), 8):  # Iterate over the binary string in chunks of 8 characters
        binary_char = binary_string[i:i+8]  # Extract each 8-bit binary character
        decoded_char = chr(int(binary_char, 2))  # Convert binary to decimal and then to character
        decoded_string += decoded_char
    return decoded_string

