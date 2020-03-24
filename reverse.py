from stack import Stack

def inserts(stack,item):
    if stack.isempty():
        stack.push(item)
    else:
        temp = stack.pop()
        inserts(stack,item)
        stack.push(temp)

def reverse(stack):
    
    if not stack.isempty():
        temp = stack.pop()
        reverse(stack)
        inserts(stack,temp)
        
        
stack = Stack()
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(7)
reverse(stack)
print(stack.printstack())
