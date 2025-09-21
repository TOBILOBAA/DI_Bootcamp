# Exercise 1: Quiz - Written in Code

class OOPQuiz:
    def what_is_class(self):
        return "A class is a blueprint for creating objects (attributes + methods)."

    def what_is_instance(self):
        return "An instance is an actual object created from a class."

    def what_is_encapsulation(self):
        return "Encapsulation is bundling data and methods in a class, restricting direct access."

    def what_is_abstraction(self):
        return "Abstraction hides implementation details and only shows essential features."

    def what_is_inheritance(self):
        return "Inheritance allows one class (child) to use attributes/methods of another (parent)."

    def what_is_multiple_inheritance(self):
        return "Multiple inheritance means a class can inherit from more than one parent class."

    def what_is_polymorphism(self):
        return "Polymorphism lets different classes use methods with the same name but different behavior."

    def what_is_mro(self):
        return "MRO (Method Resolution Order) is the order Python follows to look for methods in inheritance."


# Test
quiz = OOPQuiz()
print("1. What is a class?\n", quiz.what_is_class())
print("\n2. What is an instance?\n", quiz.what_is_instance())
print("\n3. What is encapsulation?\n", quiz.what_is_encapsulation())
print("\n4. What is abstraction?\n", quiz.what_is_abstraction())
print("\n5. What is inheritance?\n", quiz.what_is_inheritance())
print("\n6. What is multiple inheritance?\n", quiz.what_is_multiple_inheritance())
print("\n7. What is polymorphism?\n", quiz.what_is_polymorphism())
print("\n8. What is MRO?\n", quiz.what_is_mro())



import random

# Step 1: Create the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

# Step 2: Create the Deck class
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # Build 52 cards
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """Shuffle the deck if it has all 52 cards"""
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            print("Deck shuffled!")
        else:
            print("Cannot shuffle, some cards are missing.")

    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No cards left to deal!")
            return None

# Step 3: Test
deck = Deck()
print(f"Total cards: {len(deck.cards)}")  # Should be 52

deck.shuffle()

card1 = deck.deal()
print("Dealt card:", card1)

print(f"Remaining cards: {len(deck.cards)}")