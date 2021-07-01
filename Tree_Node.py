#Node for binary tree

class Node:

    def __init__(self,data) -> None:
        self.right = None
        self.left = None
        self.data = data

    def PrintTree(self): # Print in-order tree traversal
        if self.left:
            self.left.PrintTree()

        print(self.data),

        if self.right:
            self.right.PrintTree()

    def insert(self,data):
        if self.data:
            if data <= self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)



root = Node(10)
root.insert(3)
root.insert(6)
root.insert(12)
root.insert(14)
root.PrintTree()
        
