stack = r'''
# Stack in Python

A stack is a data structure that allows adding and removing elements in a particular order, LIFO (Last In, First Out).

### Stack Operations:
1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove and return the top element from the stack.
3. **Peek/Top**: Return the top element without removing it.
4. **isEmpty**: Check if the stack is empty.
5. **Size**: Get the number of elements in the stack.

### Implementation of Stack in Python
Below are two common implementations:
1. Using a Python list
2. Using `collections.deque` (preferred for performance)


```python
# 1. Stack Implementation Using List
class StackUsingList:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        """Add an element to the stack."""
        self.stack.append(item)
    
    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")
    
    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Return the size of the stack."""
        return len(self.stack)


# 2. Stack Implementation Using collections.deque
from collections import deque

class StackUsingDeque:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        """Add an element to the stack."""
        self.stack.append(item)
    
    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from an empty stack")
    
    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from an empty stack")
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Return the size of the stack."""
        return len(self.stack)


# Example Usage
if __name__ == "__main__":
    # Using list-based stack
    stack_list = StackUsingList()
    stack_list.push(10)
    stack_list.push(20)
    print("Top element (List):", stack_list.peek())  # Output: 20
    print("Size (List):", stack_list.size())  # Output: 2
    print("Popped element (List):", stack_list.pop())  # Output: 20
    print("Is empty (List):", stack_list.is_empty())  # Output: False

    # Using deque-based stack
    stack_deque = StackUsingDeque()
    stack_deque.push(30)
    stack_deque.push(40)
    print("Top element (Deque):", stack_deque.peek())  # Output: 40
    print("Size (Deque):", stack_deque.size())  # Output: 2
    print("Popped element (Deque):", stack_deque.pop())  # Output: 40
    print("Is empty (Deque):", stack_deque.is_empty())  # Output: False
```
'''
