# Day 31: Alternate Digit Math 🧮

Calculates a result by performing alternate multiplication and addition on a sequence of digits.

## 📝 Description
This complex script iterates through a string of numbers. It multiplies pairs of digits and adds the result to a running total. If a single digit remains at the end, it is added directly.

## 🛠️ Concepts Used
* **While Loops:** Iterating with manual index management and variable increments.
* **Index Jumping:** Moving the counter by 2 (`count += 2`) to process digit pairs.
* **Boundary Conditions:** Checking `count + 1 < len(s)` to prevent index out of bounds errors.

## 🚀 How to Run
```bash
python main.py