### Balanced Parentheses Checker using Stack (Array Implementation) ###

# Creating Stack class

class Stack:

    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    # s = Stack(3)

    def push(self,value):

        if self.top == self.size - 1:
            return "Stack Overflow"
        else:
            self.top += 1
            self.stack[self.top] = value # Push value onto stack

    def pop(self):

        if self.top == -1:
            return "Stack is empty"
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(data) 

    
    # traverse for printing stack elements

    def traverse(self):

        for i in range(self.top + 1):
            print(self.stack[i],end=' ')

    # s.traverse() to print stack elements