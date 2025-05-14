class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    
     def __init__(self):
        self.head=None
        self.tail=None
     def insertAtBegin(self,new_data):
        if self.head==None and self.tail==None:
            new_node=Node(new_data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(new_data)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
     def insertAtEnd(self,new_data):
        if self.head==None and self.tail==None:
            new_node=Node(new_data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(new_data)
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
            
     def findl(self):
        c=0
        temp=self.head
        while temp!=None:
            temp=temp.next
            c+=1
        return c
     def insertAtPosition(self,position,new_data):
        new_node=Node(new_data)
        if self.head==None and position==0 and self.tail==None:
            self.head=new_node
            self.tail=new_node
            return
        if self.head!=None and position==0:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.head.prev=self.tail
            self.tail.next=self.head
            return
        else:
            pl=0
            current=self.head
            while current!=None and pl<position-1:
                current=current.next
                pl+=1
            if current is None:
                raise IndexError("position is out of range")
            new_node.next=current.next
            current.next.prev=new_node
            current.next=new_node
            new_node.prev=current
    
     def delAtBegin(self):
        if self.head==None and self.tail==None:
            print("No elements to delete")
        else:
            t=self.head
            self.head=self.head.next
            t.next=None
            t.prev=None
            self.head.prev=self.tail
            self.tail.next=self.head
            del t
     def delAtEnd(self):
        if self.head==None and self.tail==None:
            print("No elements to delete")
        
        else:
            t1=self.tail
            t=self.tail.prev
            t.next=None
            self.tail.prev=None
            t1.next=None
            self.tail=t
            self.head.prev=self.tail
            self.tail.next=self.head

            del t1
     def delAtPosition(self,position):
        if self.head==None and self.tail==None:
            print("List is Empty")
        if self.head!=None and position==0:
            t=self.head
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head
            t.next=None
            t.tail=None
            del t
        else:
            pl=0
            current=self.head
            while current!=None and pl<position-1:
                current=current.next
                pl+=1
            if current is None:
                raise IndexError("Position is out of range")
            t=current.next
            current.next=current.next.next
            t.next=None
            t.prev=None
            current.next.prev=current
            del t
            
     def display_from_begin(self):
        if self.head==None and self.tail==None:
            print("Linked List is Empty")
        else:
            print("Display from Begin")
            t=self.head
            while(t!=self.tail):
                print(t.data,end=' ')
                t=t.next
            print(t.data)
     def display_from_end(self):
         if self.head==None and self.tail==None:
             print("Linked List is Empty")
         else:
             print("Display from End")
             t=self.tail
             while(t!=self.head):
                 print(t.data,end=' ')
                 t=t.prev
             print(t.data)
    
     def clock_wise(self,k):
         if self.head==None and self.tail==None:
             print("Linked List is Empty")
         else:
             temp=self.head
             
            
            
obj=DLL()
obj.insertAtBegin(10)
obj.insertAtBegin(20)
obj.insertAtBegin(30)
obj.insertAtBegin(40)
obj.display_from_begin()
print()
obj.display_from_end()
obj.insertAtEnd(50)
print()
obj.display_from_end()
print()
obj.insertAtPosition(1,60)
obj.display_from_begin()
print()
obj.delAtBegin()
obj.display_from_begin()
print()
obj.delAtEnd()
obj.display_from_begin()
print()

obj.delAtPosition(2)
obj.display_from_begin()
print()