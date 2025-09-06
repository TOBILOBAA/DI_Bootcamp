from Exercises_XP import Dog


import random 

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names =[self.name] + [dog.name for dog in args]
        if len (names) == 1:
            group = names[0]
        elif len(names) == 2:
            group = " and ". join(names)
        else:
            group = ", ".join(names[:-1]) + " and " + names[-1]
        print(f"{group} all play together")

    def do_a_trick(self):
        if not self.trained:
            print(f"{self.name} doesn't know any tricks yet. Train first!")
            return
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        print(f"{self.name} {random.choice(tricks)}!")

if __name__ =="__main__":
    fido = PetDog("Fido", 2, 20)
    buddy = PetDog("Buddy", 4, 15)
    maxy = PetDog("max", 3, 12)

    fido.do_a_trick()

    fido.train()
    fido.do_a_trick()

    fido.play(buddy, maxy)