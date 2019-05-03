"""Write a function detectAndCountLoop() that checks whether a given
Linked List contains loop and if loop is present then returns count of nodes
in loop. For example, loop is present in below linked list and length of loop
is 4. If loop is not present, then function should return 0."""


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
        temp = self.head

        while(temp):
            print(temp.key,end= "->")
            temp=temp.next

    def loopLength(self):
        """returns count of nodesin loop.If loop is not present, then function should return 0"""

        slow_p = self.head
        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                temp = slow_p
                count = 1
                slow_p = slow_p.next
                while (temp!=slow_p):
                    count += 1
                    slow_p = slow_p.next
                return count


        return False




llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)
llist.printLinkedList()

llist.head.next.next.next.next = llist.head

print("\n%d"%llist.loopLength())