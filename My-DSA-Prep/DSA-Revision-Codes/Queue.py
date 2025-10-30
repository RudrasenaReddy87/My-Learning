'''
Queue: Queue is linear data structure that follows the First In First Out (FIFO) principle.
It means that the element that is added first to the queue will be the first one to be removed.

Operations:
- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove an element from the front of the queue.
- Front: Get the front element of the queue without removing it.
- Rear: Get the last element of the queue without removing it.
- IsEmpty: Check if the queue is empty.
- IsFull: Check if the queue is full.


'''
# I nfinite (or Dynamically Growable) Array Queue
# Fixed-Size Array Queue
# Queue implementation using list

queue = [] # queue initialization
queue.append(10) # enqueue
queue.append(20) # enqueue
print(queue) # print queue
print(queue.pop(0)) # dequeue
print(queue) # print queue after dequeue
print(queue[0]) # front
print(queue[-1]) # rear
print(len(queue) == 0) # check queue is empty
def h():
    print( "---------------------------------------------------------------------------------------")
h()

# Queue using array
class Array_queue:
    def __init__(self):
        self.cap = 4
        self.queue = [0] * self.cap
        self.front = -1
        self.rear = -1
        self.cur = 0
    def enqueue(self,item):
        if self.cap == self.cur:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1)%self.cap

        self.cur += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.cur == 0:
            print("Queue is empty")
            return
        pop = self.queue[self.front]
        if self.cur == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.cap
        
        self.cur -= 1
        return pop

    def get_front(self):
        if self.front == -1:
            print("array is empty")
            return 
        return self.queue[self.front]

    def get_rear(self):
        if self.front == -1:
            print("array is empty")
            return
        return self.queue[self.rear]
    
    def __str__(self):
        if self.cur == 0:
            
            return "Queue is empty"
        if self.rear >= self.front:
            items = self.queue[self.front:self.rear+1]
        else:
            items = self.queue[self.front:] + self.queue[:self.rear+1]
        return f"front: {self.queue[self.front]} rear: {self.queue[self.rear]} total: {items} size: {self.cur}"



q1 = Array_queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.dequeue()
q1.enqueue(50)
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.front)

print(q1)