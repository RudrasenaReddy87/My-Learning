'''
author: Rudrasena Reddy
date: 04.01.2026
'''
# Linkedlist implementation in Python
'''
Linkedlist supports

- traversal
- insertion 
- deletion
- update
- searching
- reversal


Applications

Dynamic memory management
Used when size changes frequently. No need for contiguous memory like arrays.

Implementation of stacks and queues
Efficient insert and delete operations at head or tail.

Undo / Redo operations
Text editors use doubly linked lists to move backward and forward.

Browser history navigation
Each page points to previous and next pages (doubly linked list).

Music and video playlists
Next and previous song navigation.

Hash tables (chaining)
Linked lists handle collisions by storing multiple elements at the same index.

Graph adjacency lists
Each vertex stores its neighbors using linked lists.

File system navigation
Directories and subdirectories linked together.

Polynomial representation
Each node stores coefficient and power.

LRU Cache
Doubly linked list + hash map for fast access and eviction.

Circular applications
Round-robin CPU scheduling using circular linked lists.

Memory-efficient insertion/deletion
Used where frequent middle insertions/deletions are required.
'''

class Node: # creating node; we are creating node and that having data and next to store the address of another node
    def __init__(self, data): # __init__ it automatically Automatically runs at object creation Guarantees object is ready to use Prevents missing attributes. init is used to initialize an object automatically at creation, and there is no proper replacement for it in normal Python code.s
        self.data = data
        self.next = None
        
# creating the node
head = Node(10) # here we create node and links to next element
head.next = Node(20)
# when we creates the object it will be in this formate -> (<__main__.Node object at 0x00000264FFD086E0>) if we need we access .data or .next like that.
print(head.data) # prints the data if we another 20 do `Head.next`


class Linked:
    def __init__(self):
        self.head = None
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        

    def printlt(self):
        itr = ''
        cur = self.head
        while cur:
            itr += str(cur.data) + '->'
            cur = cur.next
        return itr
    
x = Linked()
x.insert(10)
x.insert(20)
x.insert(30)
x.insert(40)

print(x.printlt())
# Output: 10->20->30->40->
