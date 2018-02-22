'''


un mot français de 10 lettres dont le hash sha256 hexa contient fb80



'''


path = './dictionary.txt'
words = open(path,'r')
words = words.readlines()
import codecs

count = 0
new_words = []

with open(path) as f:
    new_words = [word.strip() for word in f]

print(len(new_words))

import hashlib

def sha_code(word):
    hash_object = hashlib.sha256(word.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

chosen_words = []
while count < len(new_words):
    word = words[count].rstrip()
    if( len(word) == 10):
        #new_words.append(word)
       # print(word[0:])
        chosen_words.append(word)

    count += 1

hashes = []
def sorted():
    for w in chosen_words:
        hash_w = sha_code(w)
        #print(w)
        hashes.append(sha_code(w))
        if ("fb80" in hash_w):
           # print("word: " +word + "hashcode: ")
            w = w.rstrip()
            #print([ord(c) for c in w])
            print("word: " +w)
            print(hash_w)



#w = "salut".encode('utf-8')
w = "cavaleries"



#print(sha_code(w))

sorted()
print(sha_code(chosen_words[1]))
print(chosen_words[1])
print(hashes[1])

#import hashlib
#hash_object = hashlib.sha256(w)
#hex_dig = hash_object.hexdigest()
#print(hex_dig)
print("sinusoidal:")
print(sha_code("sinusoidal"))
print("----------")

