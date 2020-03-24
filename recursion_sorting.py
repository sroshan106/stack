from stack import Stack


def sort(stack,temp):
    if stack.isempty() or temp>stack.peek():
        stack.push(temp)
    else:
        item = stack.pop()
        sort(stack,temp)
        stack.push(item)

def sorting(stack):
    if not stack.isempty():
        temp= stack.pop()
        sorting(stack)
        sort(stack,temp)

stack = Stack()
stack.push(4)
stack.push(1)
stack.push(8)
stack.push(3)
sorting(stack)
print(stack.printstack())
