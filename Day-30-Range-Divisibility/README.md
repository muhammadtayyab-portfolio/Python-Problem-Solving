# Day 30: Dual Range Divisibility ⚖️

Finds numbers within a range that are divisible by either of two provided numbers.

## 📝 Description
The program takes two numbers from the user, determines the range between them using `min()` and `max()`, and prints all values in that range divisible by either of the input numbers.

## 🛠️ Concepts Used
* **min/max Functions:** To correctly identify the start and end of the range regardless of input order.
* **Logical OR:** Checking divisibility using `i % num1 == 0 or i % num2 == 0`.
* **Range Function:** Generating the sequence of numbers to check.

## 🚀 How to Run
```bash
python main.py