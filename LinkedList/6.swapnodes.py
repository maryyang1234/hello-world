"""Swap nodes in a linked list without swapping data"""

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

    def swapNodes(self,x,y):

        if(x==y):
            return

        prex=None
        tempx= self.head
        while(tempx != None and tempx.key!=x):
            prex = tempx
            tempx= tempx.next

        prey = None
        tempy = self.head
        while(tempy !=None and tempy.key !=y):
            prey = tempy
            tempy = tempy.next

        if(tempx == None or tempy == None):
            print("Not both x and y are in the linkedlist")
            return



        if(prex==None):
            self.head= tempy
        else:
            prex.next = tempy

        if(prey == None):
            self.head = tempx
        else:
            prey.next = tempx

        temp=tempx.next
        tempx.next = tempy.next
        tempy.next = temp



llist = LinkedList()

# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Linked list before calling swapNodes()")
llist.printList()
llist.swapNodes(1, 7)
print("\nLinked list after calling swapNodes()")
llist.printList()