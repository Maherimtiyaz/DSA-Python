1️⃣ Overview

What it is:
Hashing is a method of mapping keys to indices in a fixed-size table using a hash function, enabling fast access to elements. It underpins many fundamental data structures like dictionaries, sets, and caches.

Why it is important:

Provides average O(1) time for insertion, search, and deletion.

Handles large datasets efficiently by avoiding linear scans.

Forms the foundation for advanced algorithms like LRU cache, substring search, and deduplication.

Where it is used:

Real-world: Password storage, URL shorteners, symbol tables in compilers, caches.

DSA context: Solving problems like two-sum, frequency counting, duplicate detection, and interval problems.

Interview relevance:
Hashing questions are common at both beginner and advanced levels. Candidates are expected to handle collisions, load factor, deletions, and performance trade-offs.

2️⃣ Core Concepts
2.1 Hash Function

Maps a key to an integer index:

index = hash(key) % table_size


Key requirements:

Deterministic: same key → same index

Uniform distribution: minimize collisions

Efficient to compute

2.2 Collisions

Occurs when two keys map to the same index.

Collision resolution strategies:

Chaining – store all keys at the same index in a linked list or array.

Open Addressing – find another empty slot using probing:

Linear probing: move sequentially

Quadratic probing: move in squares

Double hashing: use a secondary hash

2.3 Load Factor
𝛼
=
𝑛
𝑚
α=
m
n
	​


n = number of keys, m = table size.

High load factor → more collisions → slower performance.

Often, resizing occurs when α > 0.7.

2.4 Operations

Insert – add a key

Search – check for existence

Delete – remove a key

Traverse – iterate over all keys

2.5 Variations / Types
Technique	Idea	Pros	Cons
Chaining	Store multiple keys per index	Easy deletion, no clustering	Extra memory, pointers needed
Linear Probing	Move sequentially to empty slot	Cache-friendly, simple	Clustering
Quadratic Probing	Move quadratically	Reduces clustering	May fail to find slot
Double Hashing	Secondary hash function	Better distribution	More complex
3️⃣ Implementation Details
3.1 Linear Probing (Open Addressing)

Idea: On collision, move to the next index until an empty slot is found.

Pros: Simple, cache-friendly.

Cons: Clustering can degrade performance.

Complexities:

Operation	Average	Worst-case
Insert	O(1)	O(n)
Search	O(1)	O(n)
Delete	O(1)	O(n)

Python Example:

class LinearProbingHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash(key)
        while self.table[idx] is not None:
            idx = (idx + 1) % self.size
        self.table[idx] = key

    def search(self, key):
        idx = self.hash(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return True
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return False

3.2 Chaining

Idea: Each index contains a list of keys. On collision, append to the list.

Pros: Easier deletion, no clustering.

Cons: Extra memory for pointers/lists.

Complexities:

Operation	Average	Worst-case
Insert	O(1)	O(n)
Search	O(1+α)	O(n)
Delete	O(1+α)	O(n)

Python Example:

class ChainingHash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def search(self, key):
        idx = self.hash(key)
        return key in self.table[idx]

    def delete(self, key):
        idx = self.hash(key)
        if key in self.table[idx]:
            self.table[idx].remove(key)

3.3 Traversing

Linear Probing: Iterate over array, skip empty slots.

Chaining: Iterate over each bucket list.

3.4 Common Mistakes & Pitfalls

Forgetting wrap-around in linear probing.

Not handling tombstone markers for deletion.

Choosing poor hash function → clustering or uneven distribution.

High load factor → frequent collisions → slower operations.

4️⃣ Examples
Simple Example

Keys: [10, 22, 31, 4]

Table size: 10

Hash: key % 10

Key	Index
10	0
22	2
31	1
4	4
Collision Example

Keys: [10, 20], table size: 10

Hash → 10 → 0, 20 → 0 (collision)

Linear Probing: 20 → index 1

Chaining: 0 → [10, 20]

Edge Case Example

Insert keys [5, 15, 25] in table size 10 using linear probing → full table scenario → check wrap-around and search correctness.

5️⃣ Frequently Asked Questions / Traps

Deleting in linear probing: Use tombstone to avoid breaking search chain.

Full table in open addressing: Requires rehashing or resizing.

Load factor impact: α > 0.7 → more collisions, worse performance.

Linear vs Chaining: Linear probing is cache-friendly; chaining avoids clustering.

Common trick questions:

Detect duplicates in O(n) using hashing

First non-repeating character

Count frequencies or mode efficiently

Edge Cases: Empty keys, negative numbers, large ranges.

🧠 Practice Questions
🟢 Basics

Implement a hash table using chaining.

Insert, search, delete keys using linear probing.

Count frequency of elements in an array.

🟡 Intermediate

Implement double hashing for collision resolution.

Detect first non-repeating character in a string.

Implement a hash map for string keys.

Handle collisions with a custom hash function.

🔴 Advanced

Design LRU cache using hashing + doubly linked list.

Solve two-sum or subarray sum problems using hashing.

Implement dynamic resizing for hash table.

Frequency and mode queries on large datasets.

💼 Interview Questions
Conceptual

Explain collisions and handling techniques.

Compare linear probing and chaining.

How does load factor impact performance?

When should a hash table be resized?

Difference between hash map and dictionary.

Explain tombstone markers in linear probing.

Why are prime table sizes preferred?

Coding

Implement a hash table from scratch.

Detect duplicates in an array in O(n).

Find first non-repeating character in a string.

Implement LRU cache with O(1) operations.

Count element frequencies efficiently.

Company Patterns

Google: First non-repeating character, LRU cache.

Amazon: Two-sum, subarray sum, duplicate detection.

Microsoft: Implement hash map, detect collisions.

🧪 Bonus

Related topics: Dynamic resizing, perfect hashing, open addressing variations, string hashing.

Optimization tips:

Use prime-sized table for better distribution.

Choose hash function wisely for strings or composite keys.

Combine hashing with other patterns (sliding window, two pointers).

Advanced patterns: Frequency maps, memoization with hashing, hybrid approaches with arrays and sets.