#Stacks using LinkedList:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def traverse(self):
        

    def is_empty(self):
        return self.top==None
    
    def push(self, data):
        new_node = Node(data)
        if self.is_empty:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node
    


