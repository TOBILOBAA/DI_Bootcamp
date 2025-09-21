# Exercise 1: Random Sentence Generator

import random
from pathlib import Path

# Step 1: Read words from a file
def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            words = f.read().split()   # split by whitespace into list of words
        return words
    except FileNotFoundError:
        print(f"⚠️ File not found! Looked for: {file_path}")
        return []


# Step 2: Generate a random sentence
def get_random_sentence(length, file_path="words.txt"):
    words = get_words_from_file(file_path)
    if not words:  # if file was empty or missing
        return "No words available."
    
    chosen_words = [random.choice(words) for _ in range(length)]
    sentence = " ".join(chosen_words).lower()
    return sentence


# Step 3: Main function
def main():
    print("✨ This program generates a random sentence.")
    file_path = Path(__file__).resolve().parent / "words.txt"

    try:
        length = int(input("Enter a sentence length (2–20): "))
        if length < 2 or length > 20:
            print("❌ Please enter a number between 2 and 20.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    sentence = get_random_sentence(length, file_path)
    print("✅ Your random sentence is:")
    print(sentence)


if __name__ == "__main__":
    main()



# Exercise 2: Working with JSON
import json

# Step 1: Load JSON string into a Python dictionary
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)   # convert JSON string -> Python dictionary

# Step 2: Access salary
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add a birth_date key
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Step 4: Save to a file
with open("modified_employee.json", "w") as f:
    json.dump(data, f, indent=4)

print("Modified JSON saved to 'modified_employee.json'")
