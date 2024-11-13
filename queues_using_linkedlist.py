#Queues using LinkedList:


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            print('Queue is Empty')
        else:
            self.front = self.front.next

    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data)
            temp = temp.next

    def is_empty(self):
        if self.front == None:
            print('Queue is empty')
        else:
            print('Queue is Not empty')

    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter = counter + 1
            temp = temp.next
        return f"Size = {counter}" 
    
    def front_item(self): 
        if self.front == None:
            return "Queue is empty"
        else:
            return f"Front item = {self.front.data}"
        
    def rear_item(self):
        if self.front == None:
            return "Queue is empty"
        else:
            return f"Rear item = {self.rear.data}"
    
        




q = Queue()
q.enqueue(5)
q.enqueue(7)
# q.dequeue()
q.traverse()
print(q.front_item())
print(q.rear_item())
print(q.size())

# _____________________________________________________________________________________

# Famous interview question:
# Implement Queue using two stacks
