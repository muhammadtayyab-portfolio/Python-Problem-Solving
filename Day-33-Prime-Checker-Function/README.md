# Day 33: Prime Number Checker (Functional Approach) 🔢

A modular Python script to determine if a given number is prime using a custom function.

## 📝 Description
This project refines the prime number logic by wrapping it inside a function. It takes a user-provided integer and uses a `while` loop to check for divisibility. If any factor is found, it immediately concludes the number is not prime.

## 🛠️ Concepts Used
* **Functions**: Defining `prime_num_find(n)` to encapsulate the logic.
* **Early Returns**: Using `return` inside the function to exit as soon as a factor is found, making the code efficient.
* **While Loops**: Iterating through possible divisors to test primality.
* **Conditional Logic**: Handling edge cases like numbers less than or equal to 1.

## 🚀 How to Run
```bash
python main.py