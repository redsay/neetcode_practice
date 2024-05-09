class ListNode:
    def __init__(self, val, next_node=None):
        """
        Construct a node composed of a value and a pointer

        Parameters:
            - val (int) value to assign to the node
            - next_node (ListNode) pointer to the next node
        """
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        """
        Initialize an empty Linked list. The head has a value of -1 and points to none.
        The tail has a value of -1 and points to node.
        """
        self.head = ListNode(-1)
        # initializing the tail node makes it easy to insert to the tail
        self.tail = self.head

    
    def get(self, index: int) -> int:
        """
        Returns the value of the node at the specified index

        Parameters:
            - index (int) location of node value

        Returns:
            - (int) value at the index location
        """
        # initialize a counter
        i = 0
        # start at the head node
        current = self.head.next
        # loop until the ith node is equal to the index
        while current != None:
            if i == index:
                return current.val
            current = current.next
            i+=1
        # return the value at the specified index
        return -1

    def insertHead(self, val: int) -> None:
        """
        Inserts a head node into the linked list
        
        Parameters:
            - val (int) value to assign to the head node
        """
        # define a new node
        new_node = ListNode(val)
        # point the new node to where the head node is pointing
        new_node.next = self.head.next
        # point the head node to the new node
        self.head.next = new_node
        # if this is is the first node, duplicate the head and set it to the tail
        # this will allow us to insert a tail node easily
        if new_node.next == None: 
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        """
        Inserts a node to the end of the linked list

        Parameters:
            - val (int) value to insert at the end of the linked list.
        """
        # set the tail node to point to a new node
        self.tail.next = ListNode(val)
        # set the tail node to point to the new node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        """
        Removes the node at the index

        Paramters:
            - index (int) node at index to remove

        Returns
            - (bool) if the node was removed
        """
        # start a counter
        i = 0
        # start at the head node
        curr = self.head
        # look for the node pointing to the index
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> list[int]:
        """
        Obtain all values in the linked list.
        
        Returns:
            - (list) list of values in the linked list.
        """
        values = []
        current = self.head.next    
        while current :
            values.append(current.val)
            current = current.next
        return values