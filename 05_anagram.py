# Program 5: Check whether word1 and word2 are Anagrams or Not

word1 = input("Enter word1: ").replace(" ", "").lower()
word2 = input("Enter word2: ").replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print("The words are Anagrams")
else:
    print("The words are Not Anagrams")
