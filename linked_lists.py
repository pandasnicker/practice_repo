
'''
This program depicts the working of Linked list Data Structure and its operations
'''

class Node:
    # Constructor for Node
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next


class LinkedList(Node):
    # Constructor for Linked list
    def __init__(self):
        self.head = None

    def add(self, value):

        #create new node to add 
        new_node = Node(value)
        
        # check if it is the first node and add value if true
        if self.head is None:
            self.head = new_node
            return
        
        # else traverse to the end of the list and add the value to the end of list
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next

lst = LinkedList()

lst.add(1)
lst.add(2)

lst.display()