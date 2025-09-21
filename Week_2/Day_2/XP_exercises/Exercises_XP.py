# =========================
# Exercise 1: Pets & Cats
# =========================

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def walk(self):
        return f"{self.name} is walking"

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

class Simaese(Cat):  # keeping your original name
    pass


# =========================
# Exercise 2: Dogs
# =========================

class Dog:
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        # Simple formula from your code
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        # Your original comparison logic
        return self.run_speed() * self.weight - other_dog.run_speed() * other_dog.weight


# =========================
# Exercise 4: Family & Person
# =========================

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        # Fixed: return True if age >= 18
        return self.age >= 18

class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)
    
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    return ("You are over 18, your parents Jane and John accept "
                            "that you will go out with your friends")
                else:
                    return "Sorry, you are not allowed to go out with your friends."
        return "Person not found."

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"{member.first_name} {member.last_name}, {member.age} years old")


# =========================
# Exercise 3: PetDog (inherits Dog)
# =========================

import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        if len(names) == 1:
            group = names[0]
        elif len(names) == 2:
            group = " and ".join(names)
        else:
            group = ", ".join(names[:-1]) + " and " + names[-1]
        print(f"{group} all play together")

    def do_a_trick(self):
        if not self.trained:
            print(f"{self.name} doesn't know any tricks yet. Train first!")
            return
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        print(f"{self.name} {random.choice(tricks)}!")


# =========================
# Demo / Runner
# =========================

if __name__ == "__main__":
    # --- Exercise 1 demo ---
    bengal_obj = Bengal("Mikky", 4)
    chartreux_obj = Chartreux("Kate", 2)
    simaese_obj = Simaese("Lily", 3)
    sara_pets = Pets([bengal_obj, chartreux_obj, simaese_obj])
    print("== Pets walk ==")
    sara_pets.walk()

    # --- Exercise 2 demo ---
    print("\n== Dogs ==")
    dog1 = Dog("Tom", 3, 54)
    dog2 = Dog("Tim", 5, 64)
    dog3 = Dog("Jake", 2, 85)
    print(dog1.bark())
    print("Dog2 run speed:", dog2.run_speed())
    fight_score = dog1.fight(dog2)
    if fight_score > 0:
        print(f"{dog1.name} wins the fight against {dog2.name}")
    elif fight_score < 0:
        print(f"{dog2.name} wins the fight against {dog1.name}")
    else:
        print("It's a draw!")

    # --- Exercise 4 demo ---
    print("\n== Family ==")
    family = Family("Doe")
    family.members.append(Person("Jane", 35, "Doe"))
    family.members.append(Person("John", 40, "Doe"))
    family.members.append(Person("Jimmy", 16, "Doe"))
    family.born("Baby", 0)
    print(family.check_majority("Jimmy"))
    family.family_presentation()

    # --- Exercise 3 demo ---
    print("\n== PetDog ==")
    fido = PetDog("Fido", 2, 20)
    buddy = PetDog("Buddy", 4, 15)
    maxy = PetDog("Max", 3, 12)

    fido.do_a_trick()  # not trained yet
    fido.train()
    fido.do_a_trick()  # now will perform a random trick
    fido.play(buddy, maxy)