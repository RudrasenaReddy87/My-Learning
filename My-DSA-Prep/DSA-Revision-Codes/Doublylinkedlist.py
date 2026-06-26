# doubly linked list

'''
we can easily go both directions unlike linkedlist only have one direction
traverse is easy <-both directions->

-------------------------------------
|prev.address | node | next.address |
-------------------------------------

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class doub:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        cur = self.head
        new = Node(data)
        if self.head is None:
            self.head = new
            return 
        while cur.next:
            cur = cur.next
        
        cur.next = new
        new.prev = cur
    def last_delete(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.prev.next = None
        cur.prev = None

    def front_delete(self):
        cur = self.head
        self.head = cur.next
        self.head.prev = None    
    
    def delete_pos(self,pos):
        cur = self.head
        for i in range(pos-1):
            cur = cur.next
        
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
    
    def println(self):
        itr = ''
        cur = self.head
        while cur:
            itr += str(cur.data) + '<->'
            cur = cur.next
        return itr + "None"
    
d1 = doub()
d1.insert(10)
d1.insert(20)
d1.insert(30)
d1.insert(40)
d1.insert(50)
d1.delete_pos(3)
print(d1.println())