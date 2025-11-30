queue = r'''
# Queue in Python

A **queue** is a linear data structure that follows the **First In First Out (FIFO)** principle, meaning the first element added to the queue is the first one to be removed. Think of it like a line at a ticket counter: the person at the front is served first.

Python provides multiple ways to implement queues:
1. Using the `queue` module (thread-safe).
2. Using `collections.deque` (double-ended queue).
3. Using a list (not recommended for large-scale applications due to inefficiency).

---

## 1. Using the `queue` Module
The `queue` module provides three types of queues:
- **Queue**: Regular FIFO queue.
- **LifoQueue**: Last In First Out (like a stack).
- **PriorityQueue**: Queue items based on priority.

### Example: FIFO Queue
```python
import queue

# Create a FIFO Queue
q = queue.Queue()

# Add items to the queue
q.put("apple")
q.put("banana")
q.put("cherry")

# Remove items from the queue
print(q.get())  # Output: apple
print(q.get())  # Output: banana
print(q.get())  # Output: cherry
```

## 2. Using collections.deque
The deque class is highly efficient for implementing queues because it allows fast appends and pops from both ends.

### Example: Implementing a Queue with deque
```python
from collections import deque

# Create a deque
q = deque()

# Add items to the queue
q.append("apple")
q.append("banana")
q.append("cherry")

# Remove items from the queue
print(q.popleft())  # Output: apple
print(q.popleft())  # Output: banana
print(q.popleft())  # Output: cherry

```
## 3. Using a List (Inefficient)
While you can use a list to implement a queue, removing elements from the front (pop(0)) is slow for large queues because it requires shifting all subsequent elements.

### Example: Using a List as a Queue
```python
# Create a list
q = []

# Add items to the queue
q.append("apple")
q.append("banana")
q.append("cherry")

# Remove items from the queue
print(q.pop(0))  # Output: apple
print(q.pop(0))  # Output: banana
print(q.pop(0))  # Output: cherry

```
Choosing the Right Implementation
---------------------------------

-   Use the `queue` module for **thread-safe** and simpler operations in multi-threaded environments.
-   Use `collections.deque` for most other scenarios due to its speed and flexibility.
-   Avoid using a list for large-scale queue operations.
'''
