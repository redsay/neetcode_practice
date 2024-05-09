import numpy as np
class DynamicArray:
    
    def __init__(self, capacity: int):
      
        self.capacity = capacity 
        self.myArray = np.zeros(shape=capacity,dtype=int)
        self.length = 0 

    def get(self, i: int) -> int:
        return self.myArray[i]

    def set(self, i: int, n: int) -> None:
        self.myArray[i] = n
        
    def pushback(self, n: int) -> None:

        if self.length == self.capacity:
            self.resize()
        print(self.length)
        self.myArray[self.length] = n
        self.length += 1
        
        

    def popback(self) -> int:
        if self.length > 0 :self.length -= 1
        poppedBack = self.myArray[self.length]
        self.myArray = self.myArray[:self.length]
        return poppedBack

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        tmpArray = np.zeros(shape=newCapacity,dtype=int)
        tmpArray[:self.length] = self.myArray
        self.capacity = newCapacity
        self.myArray = tmpArray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
