"""Write a function which takes a list sorted in non-decreasing order and
deletes any duplicate nodes from the list.The list should only be traversed once."""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def removeDuplicates(self):

        temp = self.head
        if(temp == None):
            return None

        while( temp.next is not None):
            if(temp.data == temp.next.data):
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp=temp.next

  #      return  self.head

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
      "duplicate elements:")
llist.removeDuplicates()
llist.printList()



