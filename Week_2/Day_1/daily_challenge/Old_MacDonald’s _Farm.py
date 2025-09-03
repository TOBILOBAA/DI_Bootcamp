# Old MacDonald’s Farm

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        types = self.get_animal_types()
        animal_list = []
        for t in types:
            if self.animals[t] > 1:
                animal_list.append(t + "s")
            else:
                animal_list.append(t)
        if len(animal_list) > 1:
            animals_str =", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]
            return f"{self.name}'s farm has {animals_str}."

    




# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())          # main part
print(macdonald.get_animal_types())  # bonus 1
print(macdonald.get_short_info())    # bonus 2
#output:
# McDonald's farm

# cow : 5   
# sheep : 2
# goat : 12

#     E-I-E-I-0!
    
