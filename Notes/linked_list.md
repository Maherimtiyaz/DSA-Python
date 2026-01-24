# 📌 Linked List

## 1️⃣ Overview
- **What it is:**  
  A **Linked List** is a linear data structure where elements (nodes) are stored at **non-contiguous memory locations**. Each node points to the next node using a reference.
- **Why it is important:**  
  It overcomes limitations of arrays such as fixed size and costly insertions/deletions.
- **Where it is used:**  
  - Dynamic memory allocation  
  - Implementing stacks, queues, hash tables  
  - Undo/redo operations  
  - Memory-efficient data manipulation in DSA problems

---

## 2️⃣ Core Concepts

### Definition
- A linked list consists of **nodes**, where each node contains:
  - **Data**: value stored
  - **Next**: pointer/reference to the next node

### Key Properties
- Non-contiguous memory allocation
- Dynamic size
- Sequential access (no direct indexing)

### Types of Linked Lists
| Type | Description |
|-----|-------------|
| Singly Linked List | Node points to next node |
| Doubly Linked List | Node points to next and previous |
| Circular Linked List | Last node points to head |
| Circular Doubly LL | Combination of both |

---

## 3️⃣ Implementation Details

### Node Structure (Conceptual)

Node:
data
next

### Creating an Empty Linked List
- Initialize `head = None`

### Common Operations & Complexity

| Operation | Time Complexity |
|----------|----------------|
| Insert at Head | O(1) |
| Insert at Tail | O(n) |
| Insert at Middle | O(n) |
| Delete Head | O(1) |
| Delete Tail | O(n) |
| Search by Value | O(n) |
| Find by Index | O(n) |
| Traversal | O(n) |
| Length | O(n) |

### Language-Agnostic Pseudocode

**Insert at Head**

newNode.next = head
head = newNode


**Insert at Tail**

temp = head
while temp.next != null:
temp = temp.next
temp.next = newNode


**Delete from Head**

if head != null:
head = head.next


**Delete by Value**

prev = null
curr = head
while curr != null:
if curr.data == value:
prev.next = curr.next
break
prev = curr
curr = curr.next


### Common Mistakes & Pitfalls
- Forgetting to handle **empty list**
- Losing reference to head during insertion
- Not handling **single-node edge cases**
- Incorrect pointer updates causing memory leaks or loops

---

## 4️⃣ Examples

### Simple Example
Linked List: `10 → 20 → 30 → NULL`

- Head points to `10`
- Each node stores data + pointer

### Edge Case Example
- Empty list: `head = None`
- Single node list: `10 → NULL`

### Walkthrough (Insert at Head)
- New node = `5`
- Point `5.next` to current head (`10`)
- Update head to `5`
- Result: `5 → 10 → 20 → 30`

---

## 5️⃣ Frequently Asked Questions / Traps
- ❓ Can linked lists do random access? → **No (O(n))**
- ❓ Is insertion always O(1)? → **Only if position is known**
- ❓ Why tail deletion is slow? → **Needs second-last node**
- ❓ Why linked list uses more memory? → **Extra pointer storage**

---

## 🧠 Practice Questions

### 🟢 Basics
- Reverse a linked list
- Find length of linked list
- Insert at head and tail
- Search an element

### 🟡 Intermediate
- Delete nth node from end
- Detect loop (Floyd’s Cycle)
- Find middle of linked list
- Merge two sorted linked lists

### 🔴 Advanced
- Reverse linked list in groups of K
- Clone linked list with random pointer
- Flatten a multilevel linked list
- LRU Cache implementation

---

## 💼 Interview Questions

### Conceptual
- Difference between array and linked list
- Why linked list has no random access?
- When to prefer linked list over array?
- Singly vs doubly linked list

### Coding
- Reverse a linked list (iterative & recursive)
- Detect cycle in linked list
- Intersection point of two linked lists
- Palindrome linked list (Amazon / Microsoft)

---

## 🧪 Bonus
- **Related Topics:** Stack, Queue, Deque, Hash Table
- **Optimizations:** Maintain tail pointer for O(1) tail insertion
- **Patterns:**  
  - Two-pointer technique  
  - Slow & fast pointer  
  - Dummy node usage

