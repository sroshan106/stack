from stack import Stack
operator ='+-*/^'
def isoperator(char):
    return char in operator
    
def operation(a,b,char):
    if(char=='+'):
        return int(a)+int(b)
    elif(char=='-'):
        return int(a)-int(b)
    elif(char=='*'):
        return int(a)*int(b)
    elif(char=='/'):
        return int(a)/int(b)
    elif(char=='^'):
        return int(a)^int(b)
    
def isoperand(char):
    return char.isnumeric() and char.isnumeric()

def evaluation(expr):
    stack = Stack()
    for char in expr:
        if isoperand(char):
            stack.push(char)
        if isoperator(char):
            a = stack.pop()
            b = stack.pop()
            c = operation(a,b,char)
            stack.push(c)
    return stack.peek()

expr = '5379++'
print(evaluation(expr))
        
