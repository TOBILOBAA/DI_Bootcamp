from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker("sowpods.txt")

    while True:
        print("\n===== ANAGRAM CHECKER =====")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Goodbye!")
            break
        elif choice == "1":
            word = input("Enter a single word: ").strip()

            # Validate input
            if " " in word:
                print("❌ Error: Only one word allowed.")
                continue
            if not word.isalpha():
                print("❌ Error: Word must only contain letters.")
                continue

            # Check validity
            if not checker.is_valid_word(word):
                print(f"❌ '{word}' is NOT a valid English word.")
                continue

            # Find anagrams
            anagrams = checker.get_anagrams(word)
            print(f"\nYOUR WORD: \"{word.upper()}\"")
            print("This is a valid English word.")
            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print("No anagrams found.")

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()