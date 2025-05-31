class Node:
    def __init__(self, key):
        self.left = None
        self.right = None  # Typo fixed from 'rignt' to 'right'
        self.val = key

# Function defined outside the class
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")  # Fixed 'printt' to 'print'
    inorder(root.right)
def preorder(root):
    if root is None:
        return
    print(root.val, end=" ") 
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left) # Fixed 'printt' to 'print'
    postorder(root.right)
    print(root.val, end=" ") 


# Creating the jtree
r = Node(7)
r = insert(r, 3)  # Fixed syntax: key: 3 → 3
r = insert(r, 5)
r = insert(r, 6)
r = insert(r, 7)

# Printing inorder traversal
inorder(r)
preorder(r)
postorder(r)
