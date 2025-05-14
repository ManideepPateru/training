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
ob1=linkedlist()
ob1.traversal()
