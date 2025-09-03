# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
# cat1 = create the object
cat1 = Cat("Lily", 12)
cat2 = Cat("Tik", 24)
cat3 = Cat("micky", 22)



# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1 
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    elif cat3.age > cat1.age and cat3.age > cat2.age:
        return cat3
    else:
        return "Values are all equal"
    # ... code to find and return the oldest cat ...

# Step 3: Print the oldest cat's details    
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old")

# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name 
        self.height = height
        pass
    def bark(self):
        print(f"{self.name} does woof!")
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height}cm high ")

davids_dog = Dog("Mik", 4)
sarahs_dog = Dog("Daisey", 3)

print(f"{davids_dog.name} os {davids_dog.height}cm tall")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height}cm tall")
sarahs_dog.bark()
sarahs_dog.jump ()


# Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = [] 
        self.groups ={}
    def add_animal(self, new_animal):
        if new_animal not in self.animals:  
            self.animals.append(new_animal)
    def get_animals(self):
        print("Animals in the zoo:", self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = [animal]
            else:
                groups[first_letter].append(animal)
                self.groups = groups
    def get_groups(self):
        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
        
