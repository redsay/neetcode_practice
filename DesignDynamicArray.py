import numpy as np
class DynamicArray:
    
    def __init__(self, capacity: int):
        """
        Initialize the dynamic array with a set capacity in memory

        Parameters:
            - (int) size to set capacity in memory
        """
        self.capacity = capacity 
        # initialize the dynamic array
        self.myArray = np.zeros(shape=capacity,dtype=int)
        # initialize to zero elements in the array
        self.length = 0 

    def get(self, i: int) -> int:
        """
        Obtain the i-th index of the array

        Parameters:
            - (int) the i-th index of the array
        
        Returns:
            - (int) the i-th value of the array
        """
        return self.myArray[i]

    def set(self, i: int, n: int) -> None:
        """
        Set the i-th value of the array to the value n

        Parameters:
            - i (int) i-th index to set 
            - n (int) value to set
        """
        self.myArray[i] = n
        
    def pushback(self, n: int) -> None:
        """
        Push to the back of the array.
        Note: The back of the array is defined by the length, NOT the capacity

        Parameters:
            - n (int) value to push back
        """
        # if the dynamic array is full, double the size
        if self.length == self.capacity:
            self.resize()
        # push back n to the end
        self.myArray[self.length] = n
        # increment the number of elements
        self.length += 1
        
    def popback(self) -> int:
        """
        Remove the last element of the array and return it.
        
        Returns:
            - (int) return the popped element
        """

        # if the length == 0, the last element is the first element
        # if the length > 0, the last element is the length-1 element
        if self.length > 0 :self.length -= 1
        # get popped element
        poppedBack = self.myArray[self.length]
        # copy array, excluding popped back
        self.myArray = self.myArray[:self.length]
        return poppedBack

    def resize(self) -> None:
        """
        Double the capacity of the dynamic array
        """
        # set the size of the new capacity
        newCapacity = self.capacity * 2
        # initialize a temp array with the new capacity
        tmpArray = np.zeros(shape=newCapacity,dtype=int)
        # copy the original values to the temp array
        tmpArray[:self.length] = self.myArray
        # set the original capacity to the new capacity
        self.capacity = newCapacity
        # set the original array to the new array
        self.myArray = tmpArray

    def getSize(self) -> int:
        """
        Return the number of elements in the array

        Returns:
            - (int) 
        """
        return self.length
    
    def getCapacity(self) -> int:
        """
        Return the capacity of the array

        Returns:
            - (int) 
        """
        return self.capacity