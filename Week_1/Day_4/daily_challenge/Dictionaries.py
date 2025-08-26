user_input = input("Enter a word: ")
my_dict = {}

for index, char in enumerate(user_input):
    if char in my_dict:
        my_dict[char].append(index)
        print(f"Character {char} is a key in the dictionary")
    else: 
        my_dict[char] = [index]
        print(f"Character {char} is not a key in the dictionary")
print(my_dict)

