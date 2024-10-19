#LinkedList:

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
        temp = self.head
        self.head = self.head.next
        del temp


n = LinkList()
# n.insert_head(5)
# n.insert_head(6)
# n.insert_tail(8)
# n.insert_tail(9)
# n.insert_tail(10)
# n.insert_after(9, 100)
n.clear()
# n.delete_head()

print(n)
print(f"Number of nodes: {len(n)}")

