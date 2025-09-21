import string
import re

# -----------------
# Part I: Text Class
# -----------------
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return None
        return count

    def most_common_word(self):
        words = self.text.split()
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        # find the word with the highest count
        most_common = max(freq, key=freq.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        unique = set(words)  # removes duplicates
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return cls(content)


# -------------------------
# Part II: TextModification
# -------------------------
class TextModification(Text):
    def remove_punctuation(self):
        no_punct = ""
        for char in self.text:
            if char not in string.punctuation:
                no_punct += char
        return no_punct

    def remove_stop_words(self):
        stop_words = ["a", "the", "is", "in", "and", "of", "to"]
        words = self.text.split()
        filtered = [w for w in words if w.lower() not in stop_words]
        return " ".join(filtered)

    def remove_special_characters(self):
        cleaned = re.sub(r"[^A-Za-z0-9\s]", "", self.text)
        return cleaned


# -----------------
# Example Usage
# -----------------
if __name__ == "__main__":
    text_sample = "The cat in the hat. The cat is great!"
    txt = Text(text_sample)

    print("Word frequency of 'cat':", txt.word_frequency("cat"))
    print("Most common word:", txt.most_common_word())
    print("Unique words:", txt.unique_words())

    # Working with file
    # txt_file = Text.from_file("your_file.txt")
    # print(txt_file.most_common_word())

    # Using TextModification
    mod = TextModification(text_sample)
    print("Without punctuation:", mod.remove_punctuation())
    print("Without stop words:", mod.remove_stop_words())
    print("Without special chars:", mod.remove_special_characters())