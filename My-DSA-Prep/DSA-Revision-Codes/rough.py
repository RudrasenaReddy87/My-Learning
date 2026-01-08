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
    
    def insert_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return 
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = new
    
    def insert_pos(self, pos, data):
        new = Node(data)
        c = 0
        cur = self.head
        while cur:
            if c == pos-1:
                new.next = cur.next
                print(cur.data)
                cur.next = new
                
            c += 1
            cur = cur.next
        

    
    def insert(self,data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return 
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new
    

    def delete_begining(self):
        if self.head is None:
            return 
        cur = self.head
        cur = cur.next
        self.head = cur
    
    def delete_end(self):
        # lets take list has more values so do delete at end
        cur = self.head
        while cur.next.next:
            print(cur.data)
            cur = cur.next
        cur.next = None
    
    def delete_at_pos(self,pos):

        cur = self.head
        if pos == 0:
            self.head = cur.next
            return 
        cur = self.head
        c = 0
        while cur:
            if c==pos-1:
                cur.next=cur.next.next
            c += 1
            cur = cur.next

    def rev(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next # it stores the next number 
            cur.next = prev # it stores the prev number link(address)
            prev = cur # it stores the current number in the prev
            cur = nxt # it stores the next number in cur

        self.head = prev # at the end we put the last prev as head

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
          