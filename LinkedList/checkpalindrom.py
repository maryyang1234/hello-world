"""Given a singly linked list of characters, write a function that returns true
if the given list is palindrome,else false"""


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

def checkpalin(head):

