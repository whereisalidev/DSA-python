#stacks_using_arrays:

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size 
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack is overflowed")
        else:
            self.top = self.top + 1
            self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            del self.stack[self.top]
            self.top = self.top - 1
    
    def traverse(self):
        for i in range(self.top+1):
            print(f"{self.stack[i]} ")


        



s = Stack(2)
s.push(5)
s.push(6)
s.pop()
print(s.traverse())
