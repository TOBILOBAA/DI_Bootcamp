# Exercise 1: Pets
# class Pets():
#     def __init__(self, animals):
#          self.animals = animals
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
    
#     def walk(self):
#         return f"{self.name} is walking"

# class Bengal(Cat):
#    pass

# class Chartreux(Cat):
#    pass

# class Simaese(Cat):
#    pass

# bengal_obj = Bengal("Mikky", 4)
# chartreux_obj = Chartreux("kate", 2)
# simaese_obj = Simaese("Lily", 3)

# all_cats = [bengal_obj, chartreux_obj, simaese_obj]

# sara_pets = Pets(all_cats)

# sara_pets.walk()



# Exercise 2: Dogs
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name 
#         self.age = age 
#         self.weight = weight
    
#     def bark(self):
#         return f"{self.name} is barking"
    
#     def run_speed(self):
#         return self.weight / self.age * 10
    
#     def fight(self, other_dog):
#         return self.run_speed() * self.weight - other_dog.run_speed() * other_dog.weight
    
    
# dog1 = Dog("tom", 3, 54)
# dog2 = Dog("Tim", 5, 64)
# dog3= Dog("jake", 2, 85)

# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))


# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age <= 18:
            return True
        else:
            return False
        
class Family:
    def __init__(self, last_name, members =None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)        
        self.members.append(new_member)
    
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    return "You are over 18, your parents Jane and John accept that you will go out with your friends"
                else:
                    return "Sorry, you are not allowed to go out with your friends."

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"{member.first_name} {member.last_name}, {member.age} years old")

family = Family("Doe")
family.members.append(Person("Jane", 35))
family.members.append(Person("John", 40))
family.members.append(Person("Jimmy", 16))

family.born("Baby", 0)
print(family.check_majority("Jimmy"))
family.family_presentation()