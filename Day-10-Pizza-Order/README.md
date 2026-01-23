# Day 10: Automatic Pizza Order Program 🍕

A CLI-based ordering system that calculates the final bill based on size and extra toppings.

## 📝 Description
This program automates the price calculation for a pizza shop. It handles different base prices for sizes (S, M, L) and adds specific charges for pepperoni and extra cheese.

## 🛠️ Concepts Used
* **Multiple If-Elif-Else:** Handling various combinations of user choices.
* **Logical Operators:** Using `in ["Y", "y"]` to handle case sensitivity.
* **Accumulator Pattern:** Starting with a base price and adding to it (`price += 2`).

## 📸 Output Example
```text
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
please enter the size of pizza (S,M,L) : M
Your final bill is: $23.