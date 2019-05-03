class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def push(self,new_data):
        """ add node at the front."""
        # if self.head == None:
        #     self.head = Node(new_data)
        # else:
        #     temp = self.head
        #     self.head =Node(new_data)
        #     self.head.next = temp
        new_node = Node(new_data)
        new_node.next  = self.head
        self.head = new_node

    def insert(self,new_data,position):
        """add Node at a given position"""
        new_node = Node(new_data)
        temp = self.head
        n=1
        while n<position-1:
            if temp==None:
                print("no this position(too big) in LinkedList")
                return
            n+=1
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def append(self,new_data):
        """ add node at the end"""

        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next!=0):
            temp = temp.next
        temp.next=new_node
        
        

    def deleteNode(self, position):

        temp = self.head
        n = 1

        while n<position-1:
            if temp==None:
                print("no this position(too big) in LinkedList")
                return
            n+=1
            temp = temp.next

        del_node = temp.next
        temp.next = del_node.next

        return del_node.data


    def deleteList(self):

        current = self.head
        while current :
            prev = current.next

            del current.data

            current = prev










if __name__ == '__main__':

    l_list = LinkedList()

    l_list.head = Node(1)

    second =Node(2)
    third = Node(3)

    l_list.head.next = second
    second.next = third
    l_list.printL()

