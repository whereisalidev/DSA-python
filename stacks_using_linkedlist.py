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
        u = Stack()
        r = Stack()
        for i in str:
            u.push(i)

        for i in pattern:
            if i == 'u':
                r.push(u.pop())
            else:
                u.push(r.pop())

        res = '' 
        while not u.is_empty():
            res = u.pop() + res
        return res


        #Stacks Celebrity problem: (input: Matrix of A, B, C, D) #important
        def find_celebrity(self, matrix):
            pass


        #Balanced Brackets Problem: using stacks
        #input : mathematical expression [[(a+b)] 
        # #is the brackets opening, closing right? No -> return False
        #input : mathematical expression [[(a+b)]] 
        # #is the brackets opening, closing right? Yes -> return True

        
    

                

s = Stack()
# print(s.reverse('Hello'))
# print(s.traverse())
# print(s.text_editor('Pak', 'uur'))