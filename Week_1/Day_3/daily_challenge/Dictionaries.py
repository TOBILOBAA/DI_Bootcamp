# Challenge 1: Letter Index Dictionary

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


# Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"


upated_wallet = int(wallet.replace("$",""))
affordable_items = []

for items, price in items_purchase.items():
    cleaned_prices = int(price.replace("$","").replace(",",""))
    
    if cleaned_prices <= upated_wallet:
        affordable_items.append(items)

affordable_items = sorted(affordable_items)

if affordable_items:
    print(affordable_items)
else:
    print("Nothing")

