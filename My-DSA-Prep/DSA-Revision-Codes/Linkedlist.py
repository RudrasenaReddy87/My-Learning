'''
author: Rudrasena Reddy
date: 04.01.2026
'''
# Linkedlist implementation in Python

class Node: # creating node
    def __init__(self, data):
        self.data = data
        self.next = None
        
# creating the node
head = Node(10) # here we create node and links to next element
head.next = Node(20)
print(head.data) # prints the data if we another 20 do `Head.next`



