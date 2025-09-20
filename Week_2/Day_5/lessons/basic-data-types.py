# my_name = "Tobi"
# print(len(my_name))
# print(my_name[2])

# print(my_name.lower())

# student = "timi john"
# student2 = student.replace("i", "o")
# print(student2)


# price = "$$1$0"
# clean_price = price.strip ("$")
# print(clean_price)




# description = "strings are..."

# clean_description = description.strip(" are...")

# print((description.upper()))

# print(description.replace("are", "is"))

# print(clean_description)





# age = 35

# age += 1

# print(age)


# print (int(3.5 + 3))


# Tobis_age = 25 
# print(age * 123879)


# print("hello world!\n" * 5)

# first_name = "Tobi"
# last_name = "Ade-Ajayi"

# print(f"My name is, {first_name} {last_name}")



# user_name = input("what is your name?")
# if len(user_name) <= 5:
#     print("You have a short name :)")
# else:
#     print("You have a long name")



my_number = int(input("Give me a number between 1 and 100"))
if my_number % 3 == 0:
    print("Fizz")
elif my_number % 5 == 0:
    print("Buzz")
elif my_number % 3 == 0 and my_number % 5 == 0:
    print("FizzBuzz")
else:
    print("my_number is not divisible by 3 or 5")