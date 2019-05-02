"""Unlike linear data structures (Array, Linked List, Queues, Stacks, etc)
which have only one logical way to traverse them, trees can be traversed in
different ways. Following are the generally used ways for traversing trees."""

class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.key = val


def printInorder(root):

    if root:
        printInorder(root.left)

        print(root.key,end=" ")

        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.key,end=" ")

        printPreorder(root.right)

        printPreorder(root.left)

def printPostorder(root):

    if root:

        printPostorder(root.right)

        printPostorder(root.left)

        print(root.key,end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nPreorder traversal of binary tree is", end=" ")
printPreorder(root)

print("\nInorder traversal of binary tree is", end=" ")
printInorder(root)

print("\nPostorder traversal of binary tree is", end=" ")
printPostorder(root)

