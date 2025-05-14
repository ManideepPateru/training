class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head==None:
            print("empty list")
            return
        else:
            temp=self.head
            while temp is not None:
                print(temp.data)
                temp=temp.next
            print("null")
    def insert_at_begin(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
        
ob1=linkedlist()
ob1.insert_at_begin(1)
ob1.insert_at_begin(3)
ob1.insert_at_begin(13)
ob1.traversal()

