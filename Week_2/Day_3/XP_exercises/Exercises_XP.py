# # Exercise 1 : Hello World
# print("Hello World\n" * 4)


# # Exercise 2 : Some Math
# math = (99**3) * 8
# print(math)


# # Exercise 3 : What is the output ?
# # >>> 5 < 3 ... THIS WILL PRINT FALSE. BECUASE 5 IS NOT LESS THAN 3.
# # >>> 3 == 3 ... THIS WILL BE TRUE BECAUSE 3 IS EQUAL TO 3 
# # >>> 3 == "3" ... THIS WILL BE A FALSE BECUASE INTERGER 3 AND STRING 3 ARENT THE SAME
# # >>> "3" > 3 ... THIS WILL BE A FALSE BECAUSE STRING 3 IS NOT THE SAME AS INTERGER 3 
# # >>> "Hello" == "hello" ... THIS IS A TRUE BECAUSE STRING HELLO IS EQUAL TO STRING HELLO


# #Exercise 4 : Your computer brand

# computer_brand = "MacBook Pro"
# print(f"I have a {computer_brand} computer.")


# #Exercise 5 : Your information
# name = "Tobi"
# age = 78
# shoe_size = 45

# info = f"{name} is {age} years old, with a {shoe_size} inches shoe size and he loves humor!!"

# print(info)

# # Exercise 6 : A & B
# a = 4444
# b = 243

# if a > b:
#     print("Hello World")

# # Exercise 7 : Odd or Even
# user_input = int(input("Give me a number: "))
# if user_input % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# # Exercise 8 : What’s your name ?

# username = input("What is your name?") 

# if username == "Tobi":
#     print("oppa! we got the same name lol!")
# else:
#     print(f"Hey {username} nice to meet you!")

# # Exercise 9 : Tall enough to ride a roller coaster   

# user_height = int(input("Hey what's your height?"))

# if user_height > 145:
#     print("Congrats, you are all tall enough for the ride.")
# else:
#     print("sorry, you gonna hvae to grow some more to ride. Yikes!")


# Exercise 1: Currency (dunder methods)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # e.g., 'dollar', 'shekel'
        self.amount = amount      # integer amount

    def __str__(self):
        # Human-friendly string: e.g., "5 dollars"
        label = self.currency if self.amount == 1 else self.currency + "s"
        return f"{self.amount} {label}"

    __repr__ = __str__  # Match expected output: repr(c1) -> '5 dollars'

    def __int__(self):
        # Convert to int (just the amount)
        return int(self.amount)

    def _check_same_currency(self, other):
        if isinstance(other, Currency) and other.currency != self.currency:
            raise TypeError(
                f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
            )

    def __add__(self, other):
        # c1 + 5  OR  c1 + c2 (same currency only)
        if isinstance(other, (int, float)):
            return self.amount + other
        if isinstance(other, Currency):
            self._check_same_currency(other)
            return self.amount + other.amount
        return NotImplemented

    def __iadd__(self, other):
        # In-place add (modifies this object)
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        if isinstance(other, Currency):
            self._check_same_currency(other)
            self.amount += other.amount
            return self
        return NotImplemented
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)           # '5 dollars'
print(int(c1))      # 5
print(repr(c1))     # '5 dollars'
print(c1 + 5)       # 10
print(c1 + c2)      # 15
print(c1)           # 5 dollars

c1 += 5
print(c1)           # 10 dollars
c1 += c2
print(c1)           # 20 dollars

# print(c1 + c3)    # TypeError: Cannot add between Currency type <dollar> and <shekel>

# # Exercise 2: Import (two files)

def add_and_print(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


def add_and_print(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


# Option A:
from func import add_and_print

add_and_print(7, 13)

# Option B:
# import func
# func.add_and_print(7, 13)


# # Exercise 3: String Module (random 5-letter string)
import string
import random

def random_letters_5():
    letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Using choices (clean & concise)
    return ''.join(random.choices(letters, k=5))

# Or using a loop (as required):
def random_letters_5_loop():
    letters = string.ascii_letters
    s = ""
    for _ in range(5):
        s += random.choice(letters)
    return s

print(random_letters_5())
print(random_letters_5_loop())



# # Exercise 4: Current Date
from datetime import date

def show_today():
    today = date.today()
    print("Today is:", today.isoformat())

show_today()



# # Exercise 5: Time Until January 1st
from datetime import datetime

def time_until_jan1():
    now = datetime.now()
    next_year = now.year + 1 if (now.month, now.day) > (1, 1) or ((now.month, now.day) == (1,1) and now.time() > datetime.min.time()) else now.year
    jan1 = datetime(next_year, 1, 1, 0, 0, 0)
    delta = jan1 - now
    # Pretty print
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    print(f"Time until Jan 1 {next_year}: {days} days, {hours} hours, {minutes} minutes")

time_until_jan1()


# # Exercise 6: Birthday → Minutes Lived
from datetime import datetime

def minutes_lived(birth_str, fmt="%Y-%m-%d"):
    """
    birth_str: your birthdate as a string, e.g. "2001-04-15"
    fmt: the parsing format for strptime
    """
    dob = datetime.strptime(birth_str, fmt)
    now = datetime.now()
    delta = now - dob
    minutes = int(delta.total_seconds() // 60)
    print(f"You have lived approximately {minutes:,} minutes.")

minutes_lived("1995-10-08")  # example



# # Exercise 7: Faker Users
from faker import Faker

def generate_users(n=5):
    fake = Faker()
    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)
    return users

# Example:
users = generate_users(3)
for u in users:
    print(u)
