# 📊 Day 42: Word Frequency Counter

A Python script that analyzes a text and counts how many times each word appears.

---

## 📝 Description
This program takes a text input, converts it to lowercase, splits it into words, and then counts the occurrence of each unique word using a tracking list.

---

## 🛠️ Logic
- Text ko lowercase mein convert kiya jata hai.
- `.split()` use karke words ki list banayi jati hai.
- Ek `checked` list ka use karke har unique word ki frequency count ki jati hai.

---

## ▶️ How to Run
1. Make sure Python is installed on your system.
2. Open the project directory in a terminal.
3. Run the script:
   ```bash
   python main.py
````

4. Enter the text when prompted.

---

## 📥 Sample Input

```text
Python is easy and python is powerful
```

---

## 📤 Sample Output

```text
python : 2
is : 2
easy : 1
and : 1
powerful : 1
```
