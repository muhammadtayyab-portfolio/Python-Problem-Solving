# 6. Reverse Each Word
# Write a function reverse_words(sentence: str) -> str that reverses each word in a sentence but keeps the word order intact.
#  Example: "Python is fun" → "nohtyP si nuf"

def reverse_words(sentence):
    sentence_list = sentence.split()
    new_str = ""
    for i in sentence_list:
        new = ""
        for j in range(len(i)-1,-1,-1):
            new += i[j]
        new_str += new + " "
    return new_str

user = input("Please enter a string : ")
result = reverse_words(user)
print(result)
             