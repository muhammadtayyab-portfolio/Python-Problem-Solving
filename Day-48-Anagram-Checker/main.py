# 7. Anagram Checker
# Write a function is_anagram(str1: str, str2: str) -> bool that checks if two strings are anagrams of each other.

def is_anagram(str1 , str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print("✅ The words are anagrams!")
else:
    print("❌ The words are not anagrams.")