'''
author : Rudrasena Reddy
date : 07.12.2025

purpose : Just to practice rough work.
'''

# Rough code here

# reverse a linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
            
    def insert(self,x):
        cur = self.head
        new = Node(x)
        if self.head is None:
            self.head = new
            return # dont forget return 
        
        while cur.next:
            cur = cur.next
        cur.next = new
    
    def println(self):
        cur = self.head
        itr = ''
        while cur:
            itr += str(cur.data) + "->"
            cur = cur.next
        return itr + "None"

l1 = Linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.reverse()

print(l1.println())
        
        
