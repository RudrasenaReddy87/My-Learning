class Linked:

    def insert(self,val):
        if self.data is None:
            self.data = val
        
        cur = Node(val)
        self.data.next = cur

    def printlt(self):
        itr = ''
        while self.data:
            itr += self.data + '->'
            self.data.next
        return itr
    
x = Linked()
x.insert(10)
x.insert(20)
x.insert(30)
x.insert(40)

print(x.printlt())
