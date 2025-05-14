class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("null")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 0
        leng=0
        while temp.next!=None:
            leng=leng+1
            temp=temp.next
        temp = self.head
        if position>leng:
            print("out of indexing")
        while temp is not None:
            if count == position-1 :
                new_node.next = temp.next
                temp.next = new_node
                return
            count += 1
            temp = temp.next
        return

ob1 = LinkedList()
ele = int(input())
while ele != -1:
    ob1.insert_at_end(ele)
    ele = int(input())

ob1.traversal()

position = int(input())
new_value = int(input())
ob1.insert_at_position(position, new_value)

ob1.traversal()