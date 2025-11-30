BST_ = '''
# Binary Search Tree (BST) in Python

A **Binary Search Tree (BST)** is a node-based binary tree data structure where each node has the following properties:
1. The left subtree of a node contains only nodes with keys **less than** the node's key.
2. The right subtree of a node contains only nodes with keys **greater than** the node's key.
3. Both the left and right subtrees must also be binary search trees.

## Key Operations of a BST
- **Insertion**: Adds a new node to the tree.
- **Search**: Looks for a particular value in the tree.
- **Deletion**: Removes a node from the tree.
- **Traversals**: Different ways to visit nodes in the tree (Inorder, Preorder, Postorder).


## Complexity Analysis
- Insertion: O(h), where h is the height of the tree. In a balanced tree, `h = O(log n)`.
- Search: `O(h)`.
- Deletion: `O(h)`.
For a balanced tree, the time complexity for all operations becomes `O(log n)`.



---

## Basic Structure of a BST Node in Python

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
```
## Insertion in BST
The insertion process starts at the root and compares the value to be inserted with the current node. Based on the comparison, it either moves left or right, and this continues until an empty spot is found.
```python
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

```

### Example
```python
root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

```


## Searching in a BST
The search operation also works by comparing the target key with the current node. It moves left or right based on the comparison until the key is found or an empty node is reached.
```python
def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)


```

### Example
```python
found_node = search(root, 40)
if found_node:
    print(f"Node with key {found_node.value} found.")
else:
    print("Key not found in the tree.")

```

## Deletion in a BST
Deletion in a BST is more complex and involves three cases:

- Node with no children (a leaf node): Simply remove the node.
- Node with one child: Remove the node and replace it with its child.
- Node with two children: Find the inorder successor (smallest node in the right subtree), copy its value to the node to be deleted, and delete the inorder successor.
```python
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.value:
        root.left = deleteNode(root.left, key)
    elif key > root.value:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    return root



```

### Example
```python
root = deleteNode(root, 20)
root = deleteNode(root, 30)


```


## Height of the BST
The height of a BST is the number of edges in the longest path from the root to a leaf. It can be calculated recursively.
```python
def height(root):
    if root is None:
        return -1  # Return -1 for empty tree, 0 for a single node tree
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

```
### Example 
```python
print(f"Height of the BST: {height(root)}")

```


## BST Traversal

There are three main types of tree traversals:

### 1. Inorder Traversal (Left, Root, Right)
In an inorder traversal, nodes are visited in ascending order for a BST.
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


```

### Example
```python
inorder(root)  # Output: 20 30 40 50 60 70 80
```

### 2. Preorder Traversal (Root, Left, Right)
Preorder traversal visits the root node first, then the left subtree, followed by the right subtree.
```python
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

```

### Example
```python
preorder(root)  # Output: 50 30 20 40 70 60 80
```

### 3. Postorder Traversal (Left, Right, Root)
Postorder traversal visits the left subtree, then the right subtree, and finally the root node.
```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

```

### Example
```python
postorder(root)  # Output: 20 40 30 60 80 70 50


```



'''
