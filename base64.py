print
print("======================")
print("Writing a base64 encoder")
print("======================")

# Base64 character lookup. Translates a character to an offset, e.g. A=0, B=1, etc.
base64_lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Test string, encoded as hex ASCII values, e.g. the first two chars: '49' are 0x49, so they represent the character chr(0x49), which is 'I'. Every two hex chars represent a single text/ASCII char.
hex_str = '74686520717569636b2062726f776e20666f78206a756d7073206f76657220746865206c617a7920646f67'
print("Hex-encoded string: {}\n".format(hex_str))

# Decode hex bytes out of hex_str into string
text = hex_str.decode('hex')
print('Our string, decoded from hex: {}\n'.format(hex_str.decode('hex')))

i = 0
output = ""
# Loop over input characters, in 3-character blocks
while i < (len(text) - 3): # loop index over text, stopping at beginning of last block
    # Join current 3 characters into single 24-bit integer (3 x 8 bits = 24 bits):
    # - Shift first char 2 positions left (16 bits)
    # - Shift second char 1 position left (8 bits)
    # - Leave third char in place
    # - Merge the 3 via bitwise OR (|)
    s24bits = ord(text[i]) << 16 | ord(text[i+1]) << 8 | ord(text[i+2])
    # Now scan the 24-bit result in reverse, in 4 steps of 6 bits
    for j in range(4, 0, -1):
        mask = 0b111111 # 6-bit mask
        offset = 6 * j  # bit offset of the mask for each of the four 6-bit steps
        # Figure out index to use against base64_lookup list for the current 6-bit step
        # We do this by shifting the mask to the current 6-bit offset,
        # doing a bitwise AND to copy the bits we need for this step,
        # and finally shifting the output right to scale it down to the 0-64 range
        # in the lookup
        index = (s24bits & ( mask << offset )) >> offset
        # Find the index in the lookup and append the resulting character to the output
        output += base64_lookup[index]

    # Move input index to start of next 3-character block
    i += 3

print("Our output: {}".format(output))

# To verify your code, use the built-in base64 encoder and compare with your result
print("Correct output (built-in Base64 encoder: {}".format(hex_str.decode('hex').encode('base64')))
