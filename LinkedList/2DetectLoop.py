"""Given a linked list, check if the the linked list has loop or not.
Below diagram shows a linked list with a loop."""


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printL(self):
        temp = self.head
        while(temp):
            print(temp.data, end="")
            temp = temp.next

    def detectLoop(self):
        s=set()
        temp =self.head
        while(temp):
            if (temp in s):
                return True
            else:
                s.add(temp)
                temp=temp.next
        return False


    def detectLoop2(self):
        slow_p = self.head
        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p==fast_p:
                return True
        return False


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head;

if (llist.detectLoop()):
    print("Loop found")
else:
    print("No Loop ")


