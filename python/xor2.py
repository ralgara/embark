# https://cryptopals.com/sets/1/challenges/3

import math
import sys
import pdb
import operator
import re

c = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

map = {}

size = int(math.log(c, 16))
mask = 0xff
array = []
for i in range(int(size/2), -1, -1):
    current = ((mask << (i * 8)) & c) >> (i * 8)
    array.append(current)
    current_hex = f"{current:x}"
    #print("{0:x}".format(current))
    if current_hex in map:
        #print("Found")
        map[current_hex] = map[current_hex] + 1
    else:
        #print("Not found")
        map[current_hex] = 1

print([ f"{x:02x}" for x in array ])
#sys.exit(0)
print(sorted(map.items(), key=operator.itemgetter(1)))

p = re.compile("^[A-Za-z' ]+$")

for k in range(0,256):
    output = ""
    for current in array:
        decrypt = current ^ k
        #print(f"current: {current:02x},{current:08b}, dec: {decrypt:02x},{decrypt:0q8b}, {chr(decrypt)}")
        output += chr(decrypt)
    if p.match(output):
        print("\nKey: {0:x}".format(k))
        print(output)
