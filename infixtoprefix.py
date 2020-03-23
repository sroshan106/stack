from stack import Stack

def isoperand(char):
    return char>='A' and char<='Z'
operators ='+-*/^'
def isoperator(char):
    return char in operators
    
def getprec(char):
    result=0
    for c in operators:
        result+=1
        if(char==c):
            if char in '-/':
                result-=1
            break
    return result
def postfix(exp):
    result=''
    stack = Stack()
    
    for char in exp:
        if isoperand(char):
            result+=char
        elif isoperator(char):
            while True:
                topchar = stack.peek()
                if stack.isempty() or topchar=='(':
                    stack.push(char)
                    break;
                else:
                    pc =getprec(char)
                    ptc = getprec(topchar)
                    if(pc>ptc):
                        stack.push(char)
                        break;
                    else:
                        result+=stack.pop()
                        
                        
        elif char =='(':
            stack.push(char)
        elif char ==')':
            cpop = stack.pop()
            while cpop!='(':
                result+=cpop
                cpop=stack.pop()
    while not stack.isempty():
        cpop = stack.pop()
        result+=cpop
    return result

post = postfix('A+B*C')
print(post)
