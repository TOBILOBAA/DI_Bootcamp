user_input = input("Say whatever you want: ")
length = len(user_input)

if length < 10:
    print("String not long enough.")
elif length > 10:
    print("String too long.")
else:
    print("Perfect string")
print(user_input[0], user_input[-1])


word = "Tobi"

for i in range(1, len(word) + 1):
    print(word[:i])


               






