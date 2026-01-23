# Dynamic Array – Clean Notes

## What is a Dynamic Array?
A dynamic array is an array whose size can **change at runtime**.  
It automatically increases its capacity when the current storage becomes full.

In Python, **list** is implemented as a dynamic array.

---

## Why Do We Need Dynamic Arrays?
Static arrays have a **fixed size**, which creates two problems:
- If size is small → overflow occurs
- If size is large → memory is wasted

Dynamic arrays solve this by resizing themselves when needed.

---

## How Dynamic Array Works Internally
1. A fixed-size array is created initially
2. Elements are added until the array becomes full
3. When full:
   - A new array of larger size is created (usually double)
   - All elements are copied to the new array
   - Old array is removed
4. The reference is updated to the new array

This process is called **resizing**.

---

## Resizing Strategy
- When capacity is full, size is increased (commonly doubled)
- Resizing does NOT happen for every insertion
- It happens occasionally, which makes performance efficient overall

---

## Time Complexity of Operations

- Accessing an element: O(1)
- Updating an element: O(1)
- Insertion at end: O(1) amortized
- Insertion at index: O(n)
- Deletion from end: O(1)
- Deletion from index: O(n)

---

## Amortized Time Complexity
Although resizing takes O(n) time, it does not occur frequently.  
When averaged over many insertions, the cost per insertion becomes O(1).

This is called **amortized time complexity**.

---

## Advantages of Dynamic Arrays
- Size grows automatically
- Efficient insertion at the end
- Fast random access
- Better memory usage than static arrays

---

## Disadvantages of Dynamic Arrays
- Resizing is costly
- Insertion and deletion at arbitrary index is slow
- Extra memory is required during resizing

---

## Use Cases of Dynamic Arrays
- When size of data is unknown
- Implementing stacks and queues
- Storing dynamic collections of data
- Used internally in many programming languages

---

## Dynamic Array vs Static Array

| Feature | Static Array | Dynamic Array |
|------|------|------|
| Size | Fixed | Variable |
| Memory Usage | Can waste memory | Efficient |
| Flexibility | Low | High |
| Resizing | Not possible | Automatic |

---

## Important Interview Points
- Python list is a dynamic array
- Resizing usually doubles the capacity
- Append operation is O(1) amortized
- Dynamic arrays trade resizing cost for flexibility

## Interview Questions ⚡

Why is Python list called dynamic array?

Explain amortized complexity

When does resizing occur?

Difference between array and dynamic array?

---

## Key Takeaways
- Dynamic arrays overcome the limitation of static arrays
- They provide flexibility with efficient access
- Used heavily in real-world applications
