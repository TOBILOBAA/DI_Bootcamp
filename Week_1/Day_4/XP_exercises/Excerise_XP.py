# # Exercise 1: What Are You Learning?
# def display_message():
#     print("I am learning about funtions in Python.")
# display_message()


# # Exercise 2: What’s Your Favorite Book?
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
# favorite_book("Alice in Wonderland")


# # Exercise 3: Some Geography

# def describe_city(city, country = "Unknown"):
#     print(f"{city} is in {country}.")

# describe_city("Tel Aviv", "Israel")
# describe_city("Tel Aviv")

# # Exercise 4: Random
# import random 

# def number(num):
#     if 1 <= num <= 100:
#         random_num = random.randint(1,100)
#         if num == random_num:
#             print("Success! Number Match! YAAYYY")
#         else:
#             print(f"Fail! Your number: {num}, Random number:{random_num}")

# number(91)

# # Exercise 5: Let’s Create Some Personalized Shirts!
# def make_shirt(size = "large", text = "I love Python"):
#     print(f"Your shirt size is {size} and you {text} it well!")

# make_shirt("small", "rock")
# make_shirt("large", "I love Python")
# make_shirt("medium", "I love Python")
# make_shirt("small", "I love Java")
# make_shirt()

# Exercise 6: Magicians…
# magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

# def show_magicians(magician_names):
#     for item in magician_names:
#         print(item)
# show_magicians(magician_names)


# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] += " the Great"

# make_great(magician_names)
# show_magicians(magician_names)

# Exercise 7: Temperature Advice
import random 

def get_random_temp(month):
    if month in (12, 1, 2):
        return random.uniform(-10,10)
    elif month in (3, 4, 5):
        return random.uniform(10,10)
    elif month in (6, 7, 8):
        return random.uniform(20, 40)
    elif month in (9, 10, 11):
        return random.uniform(5, 25)
    else:
        print("Month must be an integer from 1 to 12")

def give_advice(temp):
    if temp <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif  0 < temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 == temp <= 23:
        print("Nice weather.")
    elif 24 == temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

def main():
    user_input = int(input("Enter your current month as a number (1-12): "))
    if 1 <= user_input <= 12: 
        temp = get_random_temp(user_input)
        print(f"The temperature right now is {temp}°C degree Celsius.")
    else:
        print("Invalid month!")
    
main()


