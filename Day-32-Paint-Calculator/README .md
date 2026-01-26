# Day 33: Paint Area Calculator 🎨

A functional Python tool to calculate the exact number of paint cans required based on wall dimensions.

## 📝 Description
This program takes the height and width of a wall from the user and calculates how many cans of paint are needed. Since you cannot buy a fraction of a paint can, the script uses mathematical rounding to ensure you always have enough paint.

## 🛠️ Concepts Used
* **Functions:** Defined `paint_cal(h, w)` to make the code modular and reusable.
* **Math Module:** Imported the `math` library to use `math.ceil()`, which rounds up the result to the nearest integer.
* **F-Strings:** Used for clean and readable output formatting.

## 🚀 How to Run
```bash
python problem1.py

```

## 📸 Output Example

```text
Please enter height of the wall : 3
Please enter width of the wall : 9
You'll need 6 cans of paint.
```
