# https://cryptopals.com/sets/1/challenges/2

n1 = 0x1c0111001f010100061a024b53535009181c
n2 = 0x686974207468652062756c6c277320657965
output = 0x746865206b696420646f6e277420706c6179

print("{0:x}".format(n1 ^ n2))
print("{0:x}".format(output))

