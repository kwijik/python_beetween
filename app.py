'''
un mot français de 10 lettres dont le hash sha256 hexa contient fb80

'''


path = './dictionary.txt'

new_words = []

with open(path) as f:
    for word in f:
        word = word.rstrip()  # delete invisible symbol
        if (len(word) == 10):
            new_words.append(word)
   # new_words = [word.strip() for word in f if len(word) == 10]

print("len " + str(len(new_words)))

import hashlib

def sha_code(word):
    hash_object = hashlib.sha256(word.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def sorted(array_of_words):
    for w in array_of_words:
        hash_w = sha_code(w)
        #print(w)
        if ("fb80" in hash_w):
           # print("word: " +word + "hashcode: ")
            w = w.rstrip()
            #print([ord(c) for c in w])
            print("word: " +w)
            print(hash_w)



sorted(new_words)



print("sinusoidal:")
print(sha_code("sinusoidal"))
print("----------")

