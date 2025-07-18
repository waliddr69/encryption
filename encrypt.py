import random
import string

chars = list(string.digits + string.punctuation + string.ascii_letters)


key = chars.copy()
random.shuffle(key)
user = input("enter a message")


enc_text = ""
for i in user:
    index = chars.index(i)
    enc_text += key[index]
print("encrypted text: "+enc_text)

enc_text = input("enter encrypted text: ")
user = ""
for i in enc_text:
    index = key.index(i)
    user += chars[index]

print(user)