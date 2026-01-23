import ctypes

class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C trype array with size = self.size
        self.A = self.__make__array(self.size)
    
    def __len__(self):
        return self.n
    
    # print the array
    def __str__(self):
        # create a list to hold the elements
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'
    
    # get item at index
    def __getitem__(self,index):
      if 0<= index < self.n:
        return self.A[index]
      else:
        return "Index out of range"
      return self.A[index]
    
    # create array append method
    def append(self,item):
      if self.n == self.size:
        # resize the array to double the current size
        self.__resize__(2*self.size)

        # Append the item
        self.A[self.n] = item
        self.n = self.n + 1

    # pop method
    def pop(self):
      if self.n == 0:
        return "Empty list"
        
        print(self.A[self.n-1])
        self.n = self.n - 1 

    # Clear method
    def clear(self):
        self.n = 0
        self.size = 1
        
    # Find method
    def find(self,item):
      for i in range(self.n):
        if self.A[i] == item:
            return i
        return "Value error item not in list!"
    
    # Insert method
    def insert(self,pos,item):
      if self.n == self.size:
        self.__resize__(self.size*2)

      for i in range(self.n,pos,-1):
        self.A[i] = self.A[i-1]

      self.A[pos] = item

    # Remove method
    def remove(self,item):
      pos = self.find(item)

      if type(pos) == int:
        #delete
        self.__delitem__(pos)
      else:     
         return pos



    # Delete method
    def __delitem__(self,pos):
      # delete
      if 0 <= pos < self.n: 
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]
        self.n = self.n - 1     



    # resize method
    def __resize__(self,new_capacity):
        # create a new array with new capacity
        B = self.__make__array(new_capacity)
        self.size = new_capacity

        # copy the elements from old array to new array
        for i in range(self.n):
            B[i] = self.A[i]

        # assign the new array to self.A
        self.A = B


    def __make__array(self,capacity):
        # creates a C trype array (static, referential) with size capacity
        return (capacity*ctypes.py_object)()
    
L = MeraList()
#print(L)
#len(L)
#L.append(10)
#L.append(3.4)
#L.append("Hello")
#L.append(True)
#L.append(100)
#print("Length of L:", len(L))
print(L)

