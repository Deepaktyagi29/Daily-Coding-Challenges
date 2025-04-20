# Daily-Coding-Challenges
Master common DSA patterns

# 💡 Missing in Array

## 📌 Problem Statement:
You are given an array `arr[]` of size `n - 1` that contains distinct integers in the range from `1` to `n` (inclusive). This array represents a permutation of the integers from `1` to `n` with **one element missing**. Your task is to identify and return the missing element.

### ➕ Constraints:
- 1 ≤ n ≤ 10⁶
- 1 ≤ arr[i] ≤ n
- All elements are distinct

## 🚩 Challenge:
✔️ Find the missing number efficiently in **O(n)** time and **O(1)** extra space.

## 🔍 Why It Matters?
✔️ This problem tests your ability to work with number patterns and array traversal—important for technical interviews and foundational problem solving.

## 🛠️ Solution Snapshot:
✔️ Use the **sum formula** of the first `n` natural numbers:  
`sum = n*(n+1)/2`  
Subtract the sum of given elements from this expected sum to find the missing number.

## 💻 Example:
### Input:

