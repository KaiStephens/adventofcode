# Part 1:

import hashlib
input_str = "bgvyzdsv"
hash = 0

while True:
    data = input_str + str(hash)
    md5_hash = hashlib.md5(data.encode()).hexdigest()

    if md5_hash.startswith("00000"):
        print(hash)
        break
    hash += 1

# Part 2

import hashlib
input_str = "bgvyzdsv"
hash = 0

while True:
    data = input_str + str(hash)
    md5_hash = hashlib.md5(data.encode()).hexdigest()

    if md5_hash.startswith("000000"):
        print(hash)
        break
    hash += 1