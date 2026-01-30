# 9. Count Unique Words (Ignore Case)
# Write a function count_unique_words(text: str) -> int that counts the number of unique words in a string, ignoring case.

def count_unique_words(text: str):
    text = text.lower()
    text_list = text.split()
    unique_words = set(text_list)
    return len(unique_words)   

sentence = input("Enter a sentence: ")
result = count_unique_words(sentence)
print("Number of unique words =", result)