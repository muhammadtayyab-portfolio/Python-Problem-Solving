# 1. Word Frequency Counter
# Write a function word_frequency(text: str) -> dict that takes a string as input and returns a showing how many times each word appears.

def word_frequency(text):
    words = text.lower().split()
    checked = []

    for i in words:
        if i  not in checked:
            count = words.count(i)
            print(i," -> ", count)
            checked.append(i)


user_str = input("Please enter the string : ")
word_frequency(user_str)