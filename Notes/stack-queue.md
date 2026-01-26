# 📌 Stack & Queue Implementations (Array & Linked List) — In-Depth Notes

---

## 1️⃣ Overview
- **Stack** and **Queue** are linear data structures with restricted insertion and deletion rules.
- They are fundamental for understanding **recursion, memory management, graph traversal, and scheduling**.
- Many advanced DSA problems (monotonic stack, sliding window, BFS) are built on these concepts.

### Why Important
- Frequently asked in interviews to test:
  - Pointer manipulation
  - Boundary conditions
  - Time–space trade-offs

### Usage
| Area | Application |
|----|----|
| OS | Call stack, CPU scheduling |
| Compilers | Expression evaluation, parsing |
| DSA | DFS, BFS, backtracking |
| Real-world | Undo/Redo, printer queue |

---

## 2️⃣ Core Concepts

---

## 🔹 Stack (LIFO – Last In First Out)

### Definition
- A linear data structure where insertion and deletion occur **only at one end**, called **TOP**.

### Operations
| Operation | Description |
|----|----|
| push(x) | Insert element at top |
| pop() | Remove top element |
| peek() | Get top element |
| isEmpty() | Check if empty |
| isFull() | Check if full (array stack) |

### Properties
- Restricted access
- Supports recursion
- Can cause overflow and underflow

---

## 🔹 Queue (FIFO – First In First Out)

### Definition
- A linear data structure where:
  - Insertion happens at **rear**
  - Deletion happens at **front**

### Operations
| Operation | Description |
|----|----|
| enqueue(x) | Insert at rear |
| dequeue() | Remove from front |
| front() | Get front element |
| isEmpty() | Check if empty |

### Properties
- Maintains order
- Uses two pointers (front & rear)

---

## 3️⃣ Implementation Details

---

## 🟦 Stack Using Array

### Structure
```text
arr[0...n-1]
top → index of top element

````md
# 📌 Stack & Queue Implementations — Complete Notes

---

## 🔹 Stack Using Array

### Initialization
```text
top = -1
````

---

### Push Operation

```text
push(x):
    if top == n-1:
        overflow
    top++
    arr[top] = x
```

---

### Pop Operation

```text
pop():
    if top == -1:
        underflow
    top--
```

---

### Complexity

| Operation | Time |
| --------- | ---- |
| push      | O(1) |
| pop       | O(1) |
| peek      | O(1) |
| Space     | O(N) |

---

### Pros

* Simple
* Cache friendly
* No pointer overhead

---

### Cons

* Fixed size
* Overflow possible

---

### Common Mistakes

* Missing overflow/underflow checks
* Incorrect `top` initialization

---

## 🟦 Stack Using Linked List

### Structure

```text
head → top of stack
Node = (data, next)
```

---

### Push Operation

```text
push(x):
    newNode.data = x
    newNode.next = head
    head = newNode
```

---

### Pop Operation

```text
pop():
    if head == NULL:
        underflow
    temp = head
    head = head.next
    delete temp
```

---

### Complexity

| Operation | Time                    |
| --------- | ----------------------- |
| push      | O(1)                    |
| pop       | O(1)                    |
| Space     | O(N) + pointer overhead |

---

### Pros

* Dynamic size
* No overflow (until memory exhausts)

---

### Cons

* Extra memory
* Less cache friendly

---

### Pitfalls

* Memory leaks
* Using tail instead of head

---

## 🟦 Queue Using Linked List

### Structure

```text
front → first element
rear  → last element
```

---

### Enqueue Operation

```text
enqueue(x):
    newNode.data = x
    if rear == NULL:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode
```

---

### Dequeue Operation

```text
dequeue():
    if front == NULL:
        underflow
    temp = front
    front = front.next
    if front == NULL:
        rear = NULL
    delete temp
```

---

### Complexity

| Operation | Time |
| --------- | ---- |
| enqueue   | O(1) |
| dequeue   | O(1) |
| Space     | O(N) |

---

### Edge Cases

* Dequeue last element
* Empty queue handling

---

## 4️⃣ Examples

---

### Stack Example

```text
push(5)
push(10)
push(15)
pop()
```

**Result**

```text
Top → 10 → 5 → NULL
```

---

### Queue Example

```text
enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
```

**Result**

```text
Front → 2 → 3 → NULL
Rear → 3
```

---

### Edge Case

```text
enqueue(10)
dequeue()
```

**Final State**

```text
front = NULL
rear  = NULL
```

---

## 5️⃣ Frequently Asked Questions / Traps

* Why stack operations are **O(1)**?
* Why queue needs both **front and rear**?
* Why array-based queue causes inefficiency?
* When to prefer linked list over array?

---

## 🧠 Practice Questions

### 🟢 Basics

* Implement stack using array
* Implement stack using linked list
* Implement queue using linked list

---

### 🟡 Intermediate

* Reverse string using stack
* Balanced parentheses
* Queue using two stacks

---

### 🔴 Advanced

* Next Greater Element
* Largest Rectangle in Histogram
* Sliding Window Maximum

---

## 💼 Interview Questions

### Conceptual

* Stack overflow vs underflow
* Array vs linked list stack
* Why BFS uses queue?
* Why recursion uses stack?

---

### Coding

* Min Stack
* Valid Parentheses
* LRU Cache
* Circular Queue implementation

---

## 🧪 Bonus

### Patterns

* Monotonic Stack
* Sliding Window + Queue
* Stack for recursion removal

```
```
