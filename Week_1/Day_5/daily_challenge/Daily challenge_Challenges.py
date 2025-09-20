# Step 1: Define the Function
def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()

    # Step 3: Initialize Variables
    longest = ""   # start with an empty string
    max_length = 0 # start with length 0

    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > max_length:
            longest = word
            max_length = len(word)

    # Step 6: Return the Longest Word
    return longest



# Step 1: Define the Function
def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()

    # Step 3: Initialize Variables
    longest = ""   # start with an empty string
    max_length = 0 # start with length 0

    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > max_length:
            longest = word
            max_length = len(word)

    # Step 6: Return the Longest Word
    return longest



print(longest_word("Margaret's toy is a pretty doll."))  
# Output: Margaret's

print(longest_word("A thing of beauty is a joy forever."))  

# Output: forever.

print(longest_word("Forgetfulness is by all means powerless!"))  
# Output: Forgetfulness


