import os

class AnagramChecker:
    def __init__(self, wordlist_filename):
        # Always look for the file in the same folder as this script
        base_path = os.path.dirname(__file__)
        wordlist_path = os.path.join(base_path, wordlist_filename)

        with open(wordlist_path, "r") as f:
            # Store all words in lowercase
            self.words = [line.strip().lower() for line in f]

    def is_valid_word(self, word):
        """Check if the word is valid (exists in word list)"""
        word = word.lower()
        return word in self.words

    def is_anagram(self, word1, word2):
        """Check if word2 is an anagram of word1"""
        return sorted(word1) == sorted(word2) and word1 != word2

    def get_anagrams(self, word):
        """Return all valid anagrams for the given word"""
        word = word.lower()
        return [w for w in self.words if self.is_anagram(word, w)]