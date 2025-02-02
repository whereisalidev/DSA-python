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

    def delete_mid(self):
        if self.head == None:
            print("empty Linked List")
            return
        elif self.head.next == None:
            print("There is only one node in LinkedList")
            return 

        count = 0
        curr = self.head
        curr2 = self.head

        while curr != None:
            count = count + 1
            curr = curr.next
        # print(count)
        mid = count/2

        for i in range(int(mid-1)):
            curr2 = curr2.next

        curr2.next = curr2.next.next
        



        

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
# n.insert_head(7)
n.insert_tail(9)
n.insert_tail(10)
n.insert_tail(11)
n.delete_mid()
# n.insert_after(9, 100)
# n.clear()
# n.delete_head()
# n.delete_tail()
# n.delete_value(8)
# n.search_value(8)
# n.search_by_index(3)

# print(f"Number of nodes: {len(n)}")
print(n)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


# PRACTICE PROBLEMS: LINKEDLIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            return 
        new_node = Node(data)
        new_node.next = None
        curr = self.head

        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    # Write python program to find the maximum number in a linkedlist and replace it with a given number.
    # Assume that the list contains whole no.s and there is only one maximum number.
    def replace_max(self, value):
        temp = self.head
        max = temp
        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next
        max.data = value

    # Write a method to find the sum of digits at odd positions in a linkedlist:
    def sum_of_digits(self):
        curr = self.head
        counter = 0
        sum = 0
        while curr != None:
            if counter % 2 != 0:
                sum = sum + curr.data
            counter = counter + 1
            curr = curr.next
            
        print(f"Sum = {sum}")

    # Write a program to reverse a linkedlist 
    # e.g; (before) 2->4->6   (after) 6->4->2
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = next_node
        self.head = prev_node

    #Write a func:
    #if single / or * then single space
    #if any one both (//, /*, **, */) then single space but next letter Capitalized
    #The/*sky*is//blue -> The Sky is Blue 
    def my_func(self):
        curr = self.head

        while curr.next != None:
            if curr.data == '/' or curr.data == '*':
                curr.data = ' '
                if curr.next.data == '/' or curr.next.data == '*':
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
            curr = curr.next
        



        




l = LinkedList()
# l.insert_end('T')
# l.insert_end('h')
# l.insert_end('e')
# l.insert_end('/')
# l.insert_end('*')
# l.insert_end('s')
# l.insert_end('k')
# l.insert_end('y')
# l.insert_end('*')
# l.insert_end('i')
# l.insert_end('s')
# l.insert_end('/')
# l.insert_end('/')
# l.insert_end('b')
# l.insert_end('l')
# l.insert_end('u')
# l.insert_end('e')
# l.replace_max(100)
# l.sum_of_digits()
# l.reverse()
l.my_func()
print(l)
            
'''