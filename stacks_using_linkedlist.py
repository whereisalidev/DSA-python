#Stacks using LinkedList:
'''
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

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return f"Peek: {self.top.data}"

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            self.top = self.top.next
            
    


s = Stack()
s.push(1)
s.push(2)
# s.pop()
# s.pop()
# s.pop()
s.traverse()
# print(s.peek())
'''


#---------------------------------------------------------------------------------------------------------

#STACKS: PRACTICE PROBLEMS

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
    
    # input: Hello, output: olleH
    # using Stacks

    def reverse(self, str):
        for i in str:
            new_node = Node(i)
            new_node.next = self.top
            self.top = new_node
        curr = self.top
        result = ''
        while curr != None:
            result = result + curr.data 
            curr = curr.next
        return result
                




s = Stack()
print(s.reverse('Hello'))