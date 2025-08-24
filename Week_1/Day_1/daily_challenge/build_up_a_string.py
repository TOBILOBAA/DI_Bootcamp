user_input = input("Say whatever you want: ")
length = len(user_input)

if length < 10:
    print("String not long enough.")
elif length > 10:
    print("String too long.")
else:
    print("Perfect string")
print(user_input[0]) 
print(user_input[-1])


for i in range(1, len(user_input) + 1):
    print(user_input[:i])

import random
chars = list(user_input)
random.shuffle(char)
shuffleed_string = '.'
print(user_input)    






