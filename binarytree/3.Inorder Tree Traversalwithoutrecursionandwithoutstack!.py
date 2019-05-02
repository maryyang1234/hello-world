"""Inorder Tree Traversal without recursion and without stack!"""

class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val

def printInorder(root):
    current = root

    while(current is not None):

        if(current.left is None):
            #只要当前节点没有左节点就可以打印
            print(current.key,end=" ")
            current = current.right
        else:
            temp = current.left
            while (temp.right is not None and temp.right!=current):
                temp = temp.right
            if(temp.right is None):
                temp.right = current
                current = current.left

            else:
            # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecessor恢复树的构造将节点的左子树的最右节点的后续置空
                temp.right = None
                print(current.key,end=" ")
            #当前节点的左子树都已打印，并且恢复原来状态
                current = current.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.right = Node(8)
printInorder(root)







