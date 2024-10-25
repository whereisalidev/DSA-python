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

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return f"Peek: {self.top.data}"

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
            
#---------------------------------------------------------------------------------------------------------

#STACKS: PRACTICE PROBLEMS

    # input: Hello, output: olleH
    # using Stacks
    #Time complexity O(N)
    def reverse(self, str):
        for i in str:
            self.push(i)
        result = ''
        while not self.is_empty():
            result = result + self.pop()
        return result

    
    #Text-Editor using stacks : Undo(u)-Redo(r)
    #e.g: one str and one pattern 
    #str=Pak , pattern=uru => result = Pa
    def text_editor(self, str, pattern):
        # creating two stacks; undo stack and redo stack
        
    

                

s = Stack()
print(s.reverse('Hello'))