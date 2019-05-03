"""Given a singly linked list and a key, count number of occurrences of given key
in linked list. For example, if given linked list is 1->2->1->2->1->3->1 and
given key is 1, then output should be 4"""



class Node:

    def __init__(self,data):
        self.key = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printLinkedList(self):

        temp=self.head
        while(temp):
            print(temp.key)
            temp = temp.next

    def count(self, sea_number):
        count = 0
        temp = self.head
        while(temp):
            if temp.key == sea_number:
                count += 1
            temp = temp.next
        return count

llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)

print("count of 1 is %d" %(llist.count(1)) )



