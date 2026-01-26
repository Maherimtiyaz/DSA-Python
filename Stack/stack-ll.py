# Creating Node class

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


# Creating Stack class

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None
    
    def push(self,value):

        new_node = Node(value)

        new_node.next = self.top

        self.top = new_node

    def peek(self):
        if(self.isempty()):
            return "Stack is empty"
        else:
            return self.top.data
        
    def pop(self):

        if(self.isempty()):
            return "Stack is empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def traverse(self):

        temp = self.top

        while temp != None:

            print(temp.data)
            temp = temp.next


## String Reverse using Stack ##

def reverse_string(text):

    stack = Stack()

    for i in text:
        stack.push(i)

    reversed_text = ""

    while(stack.is_empty()):
        reversed_text = reversed_text + stack.pop()

    print(reversed_text)

    #reverse_string("Hello World")


## Text Editor using Stack ##

    def text_editor(text, pattern):

        u = Stack()
        r = Stack()

        for i in text:
            u.push(i)

        for i in pattern:

            if i == 'u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)
        
        res = ""
        
        while(not u.is_empty()):
            res = u.pop() + res

        print(res)

    #  text_editor("Hello World", "uuurrru")

### Celebrity Problem using Stack ###

L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

def find_the_celeb(L):

    s = Stack()

    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:

        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            # j is not celebrity
            s.push(i)
        else:
            # i is not celebrity
            s.push(j)
            
        # print(s.traverse()) # to check stack status outcome will be 2 

        celeb = s.pop()

        for i in range(len(L)):

            if i != celeb:
                if L[i][celeb] == 0 or L[celeb][i] == 1:
                    print("No one is celebrity")
                    return 
                
        print(f"Celebrity is person {celeb}")

    # find_the_celeb(L) # to execute celebrity problem




