'''
author : Rudrasena Reddy
date : 07.12.2025

purpose : Just to practice rough work.
'''

# Rough code here

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
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
    

    def rev(self):
        cur = self.head
        prev = None
        while cur:
            # 10 -> 20
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            # 10 <- 20
        
        self.head = prev


    def println(self):
        cur = self.head
        itr = ''
        while cur:
            itr += str(cur.data) + "->"
            cur = cur.next
        return itr + "None"


lst = Linkedlist()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(40)
lst.insert(50)
lst.insert(60)
lst.rev()

print(lst.println())
          