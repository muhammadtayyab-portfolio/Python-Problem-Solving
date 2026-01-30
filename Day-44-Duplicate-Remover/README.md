# 🔁 Day 44: Duplicate Remover (No Set)

A Python script that removes duplicate elements from a list while preserving the original order.

---

## 📝 Description
This program takes a list of elements from the user and removes duplicate values **without using the `set()` function**, ensuring the original order remains unchanged.

---

## 🛠️ Logic
- Baghair `set()` function use kiye, ek khali list `unique_list` banayi jati hai.
- Loop ke zariye check kiya jata hai ke agar item pehle se `unique_list` mein maujood nahi ho, toh add kar diya jata hai.

---

## ▶️ How to Run
1. Make sure Python is installed on your system.
2. Open the project directory in a terminal.
3. Run the script:
   ```bash
   python main.py
````

4. Enter list elements separated by spaces.

---

## 📥 Sample Input

```text
1 2 2 3 4 4 5
```

---

## 📤 Sample Output

```text
Unique list: [1, 2, 3, 4, 5]
```
