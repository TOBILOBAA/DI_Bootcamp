# Challenge 1: Multiples of a Number
# give_me_a_number = int(input("Give me a number: "))
# length = int(input("How long do you want the list to be: "))

# multiples = []

# for i in range(1, length + 1):
#     multiples.append(give_me_a_number * i )
#     print(multiples)

# Challenge 2: Remove Consecutive Duplicate Letters

user_word = input("Give me any word: ")
word = ""

for char in user_word:
    if word == "" or char != word[-1]: 
        word += char 
print(word)

