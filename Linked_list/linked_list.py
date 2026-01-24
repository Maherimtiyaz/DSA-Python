# Creating Node class

class Node:

    def __init__(self,value):
       self.data = value
       self.next = None

#print(c.data)
#print(Node(5).data)  # Test code to check Node creation


# Creating Linked List class

class LinkedList:

    def __init__(self):

      # EMPTY LINKED LIST
      self.head = None
      self.n = 0
    
    def __len__(self):
      return self.n


#L = LinkedList()
#len(L)  # Test code to check length of LinkedList

# Insert head method

    def insert_head(self,value):
       
       # CREATE A NEW NODE
       new_node = Node(value)

       # create connection
       new_node.next = self.head

       # reassign head
       self.head = new_node

       # increment n
       self.n = self.n + 1

    # Traverse method

    def __str__(self):
       
       curr = self.head

       result = ''

       while curr != None:
          result = result + str(curr.data) + ' -> '
          curr = curr.next

       return result[:2]
    

#L = LinkedList()
#L.insert_head(1)
#L.insert_head(2)
#L.insert_head(3)
#L.insert_head(4)

    
    # Append method

    def append(self,value):
       
       new_node = Node(value)

       if self.head == None:
          self.head = new_node
          self.n = self.n + 1
          return


       curr = self.head

       while curr.next != None:
          curr = curr.next

          # you are at the last node
          curr.next = new_node

          self.n = self.n + 1


    # Insert in between method 

    def insert_after(self,after,value):
       
       new_node = Node(value)

       curr = self.head

       while curr != None:
          if curr.data == after:
             break
          curr = curr.next

       # case 1 break -> item fount -> curr -> not none

       if curr != None:
          # logic
          new_node.next = curr.next
          curr.next = new_node
          self.n = self.n + 1
       else:
          return "Item not found"
       
    # Delete Methods

    # List empty case

    def clear(self):
       self.head = None
       self.n = 0 

    # Delete head case

    def delete_head(self):
       
       if self.head == None:
          #empty
           return "Linked List is empty"
       
       self.head = self.head.next
       self.n = self.n - 1

    # Delete from tail(pop) case

    def pop(self):
       
       if self.head == None:
          # empty list
          return "Linked_List is empty."
       
       curr = self.head

       if curr.next == None:
          # only one element
          return self.delete_head()

       while curr.next.next != None:
          curr = curr.next

         # you are at second last node 
       curr.next = None
       self.n = self.n - 1


    # Delete by value(remove) case

    def remove(self,value):
       
       # empty list case
       if self.head == None:
            return "Linked List is empty"
       
       if self.head.data == value:
          # value is at head
            return self.delete_head()
       
       curr = self.head

       while curr.next != None:
          if curr.next.data == value:
             break
          curr = curr.next

        # case 1: value found
       if curr.next != None:
          # item not found
          return "Item not found"
       else:
         curr.next = curr.next.next

    # Search methods

    def search(self,item):
       
       curr = self.head
       pos = 0

       while curr != None:
          if curr.data == item:
             return pos
          curr = curr.next
          pos = pos + 1

          return "Item not found"
       
    # Search by index(indexing) method
    
    def __gititem__(self,value):
       
       curr = self.head
       pos = 0

       while curr != None:
          if pos == value:
             return curr.data
          curr = curr.next
          pos = pos + 1

          return "Index out of range"


    

          




