# Exercise 1: Favorite Numbers
my_fav_numbers = {2,4,6,8,10}
print(my_fav_numbers)
my_new_numbers = {12,14}
my_fav_numbers.update(my_new_numbers)
print(my_fav_numbers)
my_fav_numbers.remove(14)
print(my_fav_numbers)

friend_fav_numbers = {16,18,20}
our_fav_number = my_fav_numbers | friend_fav_numbers
print(our_fav_number)


# Exercise 2: Tuple
my_tuple = (1,2,3,4)
list_tuple = (list(my_tuple))
print(list_tuple)
my_string = [5,6,7,8,9,10]
add_tuple = list_tuple + my_string
print(tuple(add_tuple))


# Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
basket.clear()
print(basket)


# Exercise 4: Floats
my_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
for i in my_list:
    print(my_list)
print("Yes, you can generate this sequence using a loop did not try another method.")


# Exercise 5: For Loop
mlist = range(21)
for i in mlist:
    print(i)

for i in mlist:
    if i % 2 == 0:
        print(i)

# Exercise 6: While Loop
user_input = input("Enter your name!")
while user_input != "Tobi":
    user_input = input("Enter your name!")


# Exercise 7: Favorite Fruits
user_input = input("Please input your favorite fruits separated by spaces.")
fruits = []
fruits.append(user_input)
print(fruits)
user_input2 = input("Please input a name of any fruit")
if user_input2 in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8: Pizza Toppings
base_price = 10
topping_price = 2.50
toppings = []  

while True:
    user_input = input("Enter a topping (or 'quit' to finish): ")
    if user_input.lower() == "quit":
        break
    print(f"Adding {user_input} to your pizza.")
    toppings.append(user_input) 

total_cost = base_price + (len(toppings) * topping_price)

print("Your pizza will have these toppings:", toppings)
print("Number of toppings:", len(toppings))
print("Total cost: $",total_cost)


# Exercise 9: Cinemax Tickets
total_cost = 0

while True:
    age_input = input("Enter the age of a family member (or 'done' to finish): ")

    if age_input.lower() == "done":
        break   

    age = int(age_input) 

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price  

print(f"The total ticket cost for the family is: ${total_cost}")


# Bonus 
attendees = []

while True: 
    age_input = input("Enter age (or 'done' to finish): ")

    if age_input.lower() == "done":
        break

    age = int(age_input)

    if 16 <= age <=21:
        attendees.append(age)
    else: 
        print(f"Age {age} not allowed")
print("Final list of attendees:", attendees)


# Exercise 10: Sandwich Orders
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
item_to_remove = ["Pastrami"]
new_sandwich_orders = [item for item in sandwich_orders if item not in item_to_remove]
index = 0 
finished_sandwiches = []

while index < len(new_sandwich_orders):
    sandwich = new_sandwich_orders[index]
    finished_sandwiches.append(sandwich)
    print(f"i made you a {finished_sandwiches}")
    index += 1





