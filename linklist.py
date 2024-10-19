#LinkedList:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkList:

    def __init__(self):
        self.head = None
        self.n = 0


    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_tail(self, data):
        new_node = Node(data)


    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]


n = LinkList()
n.insert_head(5)
n.insert_head(6)
n.insert_head(7)

print(n)