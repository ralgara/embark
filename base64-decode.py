"""
dGh IHF aWN IGJ b3d IGZ eCB dW1 cyB dmV IHR ZSB YXp IGR
dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZw==
"""


import base64
import pdb

print
print("======================")
print("Writing a base64 encoder")
print("======================")

# *********** NOTE: this version isn't quite right yet. Need to add padding logic to insert required '='s to fill the last block

# Base64 character lookup. Translates a character to an offset, e.g. A=0, B=1, etc.
base64_lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Test string, encoded as hex ASCII values, e.g. the first two chars: '49' are 0x49, so they represent the character chr(0x49), which is 'I'. Every two hex chars represent a single text/ASCII char.
hex_str = '74686520717569636b2062726f776e20666f78206a756d7073206f76657220746865206c617a7920646f67'
print("Hex-encoded string: {}\n".format(hex_str))

# Decode hex bytes out of hex_str into string
text = hex_str.decode('hex')
print('Our string, decoded from hex:\n{}\n'.format(text))
print('len(text): {}'.format(len(text)))


def pbinary(n):
    print("{0:b}".format(n))

i = 0
output = ""
# Loop over input characters, in 3-character blocks
#while i < (len(text) - 3): # loop index over text, stopping at beginning of last block
for i in range(0, len(text), 3):
    # Join current 3 characters into single 24-bit integer (3 x 8 bits = 24 bits):
    # - Shift first char 2 positions left (16 bits)
    # - Shift second char 1 position left (8 bits)
    # - Leave third char in place
    # - Merge the 3 via bitwise OR (|)

    s24bits = ord(text[i]) << 16
    padding = 0

    # Encode each char in current block, catching index errors if block goes beyond
    # end of input string. Padding variable records how many padding chars are needed
    try:
        s24bits = s24bits | ord(text[i+1]) << 8
    except IndexError:
        padding = 1
    try:
        s24bits = s24bits | ord(text[i+2])
    except IndexError:
        padding = 2

    print("i:{0}, block:{1}".format(
        i, text[i:i+3]))
    print("s24bits:{0:024b}".format(s24bits))
    # Now scan the 24-bit result in reverse, in 4 steps of 6 bits
    #import pdb; pdb.set_trace()
    for j in range(3, -1, -1):
        mask = 0b111111 # 6-bit mask
        offset = 6 * j  # bit offset of the mask for each of the four 6-bit steps
        # Figure out index to use against base64_lookup list for the current 6-bit step
        # We do this by shifting the mask to the current 6-bit offset,
        # doing a bitwise AND to copy the bits we need for this step,
        # and finally shifting the output right to scale it down to the 0-64 range
        # in the lookup
        print("{0} mask:{1:24b}".format(j, mask << offset))
        index = (s24bits & ( mask << offset )) >> offset

        if padding > 0 and padding > j:
            # Add padding = if needed
            output += "="
        else:
            # Find the index in the lookup and append the resulting character to the output
            output += base64_lookup[index]

    # Move input index to start of next 3-character block
    #i += 3

print("Our output:\n{}".format(output))

# To verify your code, use the built-in base64 encoder and compare with your result
encoded = base64.b64encode(hex_str.decode('hex'))
print("Correct output (built-in Base64 encoder):\n{}".format(encoded))
