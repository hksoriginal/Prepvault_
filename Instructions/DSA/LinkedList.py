ll_ds = r'''

# Linked List in Python

## What is a Linked List?

A linked list is a linear data structure in which elements, called nodes, are connected using pointers. 
Each node contains:
1. **Data**: The value stored in the node.
2. **Next**: A reference (pointer) to the next node in the sequence.

Unlike arrays, linked lists are not stored in contiguous memory locations. This makes linked lists dynamic and allows for efficient insertion and deletion of elements.

---

## Types of Linked Lists:
1. **Singly Linked List**: Each node points to the next node, and the last node points to `None`.
2. **Doubly Linked List**: Each node has two references, one to the next node and one to the previous node.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

---

## Structure of a Node
```python
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# Example: Create a node
node1 = Node(5)
print(node1.data)  # Output: 5
print(node1.next)  # Output: None
```

## Singly Linked List Example
A singly linked list links nodes sequentially in one direction.

```python
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

    def display(self):
        """Print all elements in the list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None
```


## Doubly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    def append(self, data):
        """Add a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        """Display the list in forward direction"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display the list in backward direction"""
        current = self.head
        if not current:
            print("None")
            return
        while current.next:  # Traverse to the last node
            current = current.next
        while current:  # Traverse backward to the head
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Forward:")
dll.display_forward()  # Output: 10 <-> 20 <-> 30 <-> None
print("Backward:")
dll.display_backward()  # Output: 30 <-> 20 <-> 10 <-> None

```

## Circular Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    def append(self, data):
        """Add a new node to the circular linked list"""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = self.head  # Point back to itself
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Make it circular

    def display(self):
        """Display the circular linked list"""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Stop when we loop back to the head
                break
        print("(back to head)")


# Example Usage
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()  # Output: 10 -> 20 -> 30 -> (back to head)

```

'''
