### CLASS QUEUE
# represents a FIFO ADT

class Queue():

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    #O(n)
    def enqueue(self,item):
        self.items.insert(0,item)

    #O(1)
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def testQ():
    q = Queue([1,2])
    print q.dequeue()
    q.enqueue(5)
    q.enqueue(6)
    print q.dequeue()
    print q.dequeue()
    print q.is_empty()

if __name__ == '__main__':
    testQ()


