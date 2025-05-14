class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class binarytree:
    def insertnode(self,value):
        if root is None:
            newnode=Node(value)
            root = newnode()
        else:
            newnode=Node(value)
            temp=root.data
            while temp.left is None and temp.right is None:
                temp.left=Node(value)
        