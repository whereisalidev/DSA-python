"""
#LinkedList:
#Singly Linked List:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkList:

    def __init__(self):
        self.head = None
        self.n = 0


    def __len__(self):
        return self.n


    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def insert_tail(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.n = self.n + 1
            return 
        new_node = Node(data)
        new_node.next = None
        curr = self.head

        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, data):
        new_node = Node(data)
        curr = self.head
        while curr != None and curr.data != after:
            curr = curr.next

        if curr == None:
            print(f"Number {after} not found in this linked list")
            return
            
        new_node.next = curr.next
        curr.next = new_node
        self.n = self.n + 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    def clear(self):
        if self.head == None:
            print("List is empty")
            return 
        curr = self.head
        while curr != None:
            temp = curr.next
            del curr
            curr = temp
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            print("List is empty")
            return 
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_tail(self):
        if self.head == None:
            print("List is empty")
            return
        
        if self.head.next == None: #means we ahve only 1 node:
            return self.delete_head()    
        
        curr = self.head
        while curr.next.next != None:
            curr = curr.next

        temp = curr.next
        curr.next = None
        del temp

    def delete_value(self, value):
        if self.head == None:  
            print("List is empty")
            return
        if self.head.data == value:  #if list has only one node or the value is in first node
            return self.delete_head()
        
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            print("Value not found")
            return
        temp = curr.next
        curr.next = curr.next.next
        del temp


    def search_by_value(self, value):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == value:
                print(f"Value found at index {pos}")
                return
            curr = curr.next
            pos = pos+1
        print("Value not found")

    def search_by_index(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                print(f"{curr.data} value in at index {pos}")
                return
            curr = curr.next
            pos = pos + 1
        
        print(f"Index is out of range of list")





        

n = LinkList()
# n.insert_head(5)
# n.insert_head(6)
# n.insert_tail(8)
# n.insert_tail(9)
# n.insert_tail(11)
# n.insert_after(9, 100)
# n.clear()
# n.delete_head()
# n.delete_tail()
# n.delete_value(8)
# n.search_value(8)
# n.search_by_index(3)

# print(f"Number of nodes: {len(n)}")
print(n)
"""