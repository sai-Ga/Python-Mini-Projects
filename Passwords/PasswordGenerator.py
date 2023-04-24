import random 
import string
password=''
print('welcome to password generator')
words=[random.choice(string.ascii_letters) for i in range(int(input('enter how many letters')))]
numbers=[random.choice(string.digits) for i in range(int(input('enter how many numbers')))]
symbol=[random.choice(string.punctuation) for i in range(int(input('enter how many symbols')))]
key=words+numbers+symbol
random.shuffle(key)
for i in key:
    password=password+i
print(password)