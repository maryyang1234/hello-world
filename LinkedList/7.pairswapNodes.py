"""Given a singly linked list, write a function to swap elements pairwise.
For example, if the linked list is 1->2->3->4->5 then the function should
change it to 2->1->4->3->5, and if the linked list is 1->2->3->4->5->6
then the function should change it to 2->1->4->3->6->5."""


class Node:
    def __init__(self,data):
        self.key = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.key,end=" ")
            temp=temp.next


    def pairswap(self):
        temp = self.head

        if temp==None:
            return

        while(temp != None and temp.next !=None):
            n = temp.key
            temp.key = temp.next.key
            temp.next.key = n

            temp=temp.next.next


llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Linked list before calling pairWiseSwap() ")
llist.printList()

llist.pairswap()

print("\nLinked list after calling pairWiseSwap()")
llist.printList()
