from stack import Stack


def enqueue(stack,data):
    stack.push(data)

def dequeue(stack,stack1):
    
    if stack1.isempty():
        while not stack.isempty():
            stack1.push(stack.pop())

    return stack1.pop()
def printq(stack,stack1):
    for i in stack1.printstack():
        print(i,end = ' ')
    for i in stack.printstack():
        print(i,end =' ')

stack = Stack()
stack1 = Stack()
data ='a'
enqueue(stack,data)
enqueue(stack,'b')
dequeue(stack,stack1)
enqueue(stack,'c')
dequeue(Stack,stack1)
enqueue(stack,'d')
printq(stack,stack1)
