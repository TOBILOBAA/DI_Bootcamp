# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_tickets = 0
for names, ages in family.items(): 
    if ages < 3:
        amount = 0
    elif ages >= 3 and ages <= 12:
        amount = 10
    else:
        amount = 15
    print(f"{names}'s ticket price: ${amount}")
    total_tickets += amount
print(total_tickets)

# Bonus
names = input("Please input the names of your families seperated but commas: ").split(",")
ages = input("Please input the ages of your family members consecively seperated but commas: ").split(",")

names = [n.strip() for n in names]
ages = [int(a.strip())for a in ages]

family_dict = dict(zip(names, ages))

total_tickets = 0
for names, ages in family_dict.items(): 
    if ages < 3:
        amount = 0
    elif ages >= 3 and ages <= 12:
        amount = 10
    else:
        amount = 15
    print(f"{names}'s ticket price: ${amount}")
    total_tickets += amount
print(total_tickets)

# Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
            "France": "blue",
            "Spain": "red",
            "US": ["pink", "green"]
    }        
}

brand.update({"number_stores": 2})
print(brand)

print(f"{brand["name"]} has clothes for {brand["type_of_clothes"]}, check them out!")

brand.update({"country_creation": "Spain"})
print(brand)

if "international_competitors" in brand:
    brand.update({"international_competitors": "Desigual"})
    print(brand)

del brand["creation_date"]
print(brand)

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

for keys in brand.keys():
    print(keys)


# Bonus
more_on_zara = {
    "creation_date": 2025,
    "number_stores": 8,
}

brand.update(more_on_zara)
print(brand)


# Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dict1 = {name: index for index, name in enumerate(users)}
print(dict1)

dict2 = {index: name for index, name in enumerate(users)}
print(dict2)

sorted_users = sorted(users)
dict3 = {name: index for index, name in enumerate(sorted_users)}
print(dict3)