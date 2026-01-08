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

    def insert_begining(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        cur = self.head
        new.next = cur
        self.head = new
    
    def insert_end 
    
    def insert(self,data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return 
        cur = self.head
        cur.next = new
    
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
lst.insert_begining(50)
lst.insert_begining(100)
print(lst.println())
          