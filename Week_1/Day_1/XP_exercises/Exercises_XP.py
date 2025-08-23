# Exercise 1 : Hello World
print("Hello World\n" * 4)


# Exercise 2 : Some Math
math = (99**3) * 8
print(math)


# Exercise 3 : What is the output ?
# >>> 5 < 3 ... THIS WILL PRINT FALSE. BECUASE 5 IS NOT LESS THAN 3.
# >>> 3 == 3 ... THIS WILL BE TRUE BECAUSE 3 IS EQUAL TO 3 
# >>> 3 == "3" ... THIS WILL BE A FALSE BECUASE INTERGER 3 AND STRING 3 ARENT THE SAME
# >>> "3" > 3 ... THIS WILL BE A FALSE BECAUSE STRING 3 IS NOT THE SAME AS INTERGER 3 
# >>> "Hello" == "hello" ... THIS IS A TRUE BECAUSE STRING HELLO IS EQUAL TO STRING HELLO


#Exercise 4 : Your computer brand

computer_brand = "MacBook Pro"
print(f"I have a {computer_brand} computer.")


#Exercise 5 : Your information
name = "Tobi"
age = 78
shoe_size = 45

info = f"{name} is {age} years old, with a {shoe_size} inches shoe size and he loves humor!!"

print(info)

# Exercise 6 : A & B
a = 4444
b = 243

if a > b:
    print("Hello World")

# Exercise 7 : Odd or Even
user_input = int(input("Give me a number: "))
if user_input % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Exercise 8 : What’s your name ?

username = input("What is your name?") 

if username != "Tobi":
    print("oppa! we got the same name lol!")
else:
    print(f"Hey {username} nice to meet you!")

# Exercise 9 : Tall enough to ride a roller coaster   

user_height = int(input("Hey what's your height?"))

if user_height > 145:
    print("Congrats, you are all tall enough for the ride.")
else:
    print("sorry, you gonna hvae to grow some more to ride. Yikes!")
64


