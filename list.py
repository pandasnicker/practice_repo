# program to traverse a list data structure

from collections.abc import Iterable

class Node(object):

    def __init__(self, next = None, value = 0):
        self.next = next
        self.value = value
    
    def getElement(self):
        return self.value
    
    def setElement(self, value):
        self.value = value
        
class Lists(Node):
    head = None

    def __init__(self):
        self.head = super.Node()

    def create(self, *values):
        head = Node()
        temp = head
        if isinstance(values[0],Iterable):
            for x in values[0]:
                temp.next = None
                temp.value = x
            _head = head
            return head
        else:
            return Node(None,values[0])

    def traverse(self):
        while head.next:
            if head.next.next != None:
                print(head.value + "->")
            else:
                print(head.value)

    def getHead(self):
        pass

    def lastValue(self, head):
        while head.next:
            head = head.next
        return head.value

if __name__ == "main":
    l1 = Lists()
    l1.create([1,2,3,4])
    l1.traverse