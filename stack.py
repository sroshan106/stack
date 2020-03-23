	class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isempty():
            return self.items[-1]
    def isempty(self):
        return self.items==[]
    def printstack(self):
        return self.items
'''ob = Stack()
ob.push('A')
ob.push('B')
ob.push('c')
print(ob.printstack())
ob.pop()
print(ob.printstack())
ob.push('D')
print(ob.printstack())
ob.pop()
print(ob.printstack())
print(ob.isempty())
print(ob.peek())
'''