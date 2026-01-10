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
    

lst = Dlinkedlist()



