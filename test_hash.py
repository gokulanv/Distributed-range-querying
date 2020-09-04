def hash_string(id, PRIME):
    num = 0
    for i in id:
        num = (num*PRIME + ord(i))%PRIME
    return num

print(hash_string('aa', 53))
print(hash_string('az', 53))
print(hash_string('abb', 53))
print(hash_string('abc', 53))
print(hash_string('azz', 53))
print(hash_string('aafa', 53))
print(hash_string('aavafvaFAwf', 53))
# print(hash_string('aaa', 53))
# print(hash_string('aaa', 53))
# print(hash_string('aaa', 53))
# print(hash_string('aaa', 53))