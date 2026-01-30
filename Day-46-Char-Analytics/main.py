# Count Characters
#  Write a function count_characters(text: str) -> dict that counts uppercase, lowercase, digits, and special characters in a string and returns the result .

def count_characters(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1

    return uppercase, lowercase, digits, special

# Example usage:
text = "Hello World! 123"
upper, lower, digit, special = count_characters(text)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special characters:", special)


