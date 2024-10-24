#Stacks using LinkedList:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next

    def is_empty(self):
        return self.top==None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
# print(s.is_empty())