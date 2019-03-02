phrase = ''
phrase[0:3]
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_decoded_str = hex_str.decode('hex')

i = 0
output = ""
while i < len(phrase):
    print(phrase[i:i+3])
    b64 = ord(phrase[i]) * 2**16 + ord(phrase[i+1]) * 2**8 + ord(phrase[i+2])
    mask = 0b000000000000000000111111
    t0 = b64 & mask
    t1 = (b64 & (mask << 6)) >> 6
    t2 = (b64 & (mask << 12)) >> 12
    t3 = (b64 & (mask << 18)) >> 18
    output += l[t0] + l[t1] + l[t2] + l[t3]
    i += 3

print(output)
