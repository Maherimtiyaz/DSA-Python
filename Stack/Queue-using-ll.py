### Queue using linked list ###

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if self.front == None:
            return "Queue is empty"
        else:
            self.front = self.front.next

    def is_empty(self):
        return self.front == None

    def size(self):
        temp = self.front
        counter = 0

        while temp != None:
            counter += 1
            temp = temp.next

        return counter
    
    def peek(self):
        if self.front == None:
            return "Queue is empty"
        else:
            return self.front.data
        
    def front_item(self):
        if self.front == None:
            return "empty"
        else:
            return self.front.data
        
    def rear_item(self):
        if self.rear == None:
            return "empty"
        else:
            return self.rear.data
 
    # traverse for printing queue elements

    def traverse(self):

        temp = self.front

        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next 

    # q = Queue()

    # q.enqueue(4)
    # q.enqueue(5)
    # q.enqueue(6)
    # q.enqueue(7)

    # q.traverse()
    # print()
    # q.dequeue()
    # q.traverse()
    #q.empty()