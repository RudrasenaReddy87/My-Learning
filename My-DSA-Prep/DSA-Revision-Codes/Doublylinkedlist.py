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
        self.next = self.prev = None
    
class Dlinkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return 
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = new
        new.prev = cur
        

        
    def println(self):
        cur = self.head
        itr = ''
        while cur:
            itr += str(cur.data)+"<->"
            if cur and cur.next and cur.prev:
                print("cur : ",cur.data)
                print("prev : ",cur.prev.data)
                print("next : ",cur.next.data)
            cur = cur.next

        return itr + "None"

        


dlst = Dlinkedlist()
dlst.insert(10)
dlst.insert(20)
dlst.insert(30)
dlst.insert(40)
dlst.insert(50)
print(dlst.println())

