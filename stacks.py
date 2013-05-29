### CLASS STACK
# represent a LIFO abstract data structure.

class Stack():
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


### ---- SIMPLE ALGORITHMS WITH STACK ---- ###

#DivideBy2
#in: decimal number
#out: binary string
#while decimal we divided by 2 and store the mod in stack,
#the reverse of stack at the end represent the binary of it.
def divideBy2(decimal):
    modStack = Stack()

    while decimal > 0:
        modStack.push(decimal % 2)
        decimal = decimal // 2

    binary = ''
    while not modStack.is_empty():
        binary += str(modStack.pop())

    return binary

def main():
    print divideBy2(8)

def main1():
    s = Stack([1, 2, 3, 5])
    while not s.is_empty():
        print s.pop()

if __name__ == '__main__':
    main()