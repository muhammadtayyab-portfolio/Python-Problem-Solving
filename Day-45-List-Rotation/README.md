# 🔄 Day 45: List Rotation

A Python script that rotates a list to the right by `k` steps using list slicing.

---

## 📝 Description
This program takes a list of elements and a rotation value `k`, then rotates the list to the right while maintaining the relative order of elements.

---

## 🛠️ Logic
- `k % len(lst)` use kiya jata hai taake rotation list ki length se zyada na ho.
- List slicing `lst[-k:] + lst[:-k]` ke zariye elements ki positions rotate ki jati hain.

---

## ▶️ How to Run
1. Ensure Python is installed on your system.
2. Open the project directory in a terminal.
3. Run the script:
   ```bash
   python main.py
````

4. Enter list elements and rotation value when prompted.

---

## 📥 Sample Input

```text
List: 1 2 3 4 5
k: 2
```

---

## 📤 Sample Output

```text
Rotated list: [4, 5, 1, 2, 3]
```

