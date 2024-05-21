class ListNode:
    def __init__(self, val, next=None, prev=None):

        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = ListNode(-1,None,None)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next==self.tail
    
    def append(self, value: int) -> None:
        
        NewNode = ListNode(value) # define the new node to add
        PrevNode = self.tail.prev # intialize the last node 

        PrevNode.next = NewNode # last --> new
        NewNode.prev = PrevNode # last <-- new

        NewNode.next = self.tail # new --> tail
        self.tail.prev = NewNode # new <-- tail

    def appendleft(self, value: int) -> None:

        NewNode = ListNode(value)   # Node to add
        NextNode = self.head.next   # First node on left

        NextNode.prev = NewNode     # Point original first node to new node
        NewNode.next = NextNode     # Point new node to the original node

        self.head.next = NewNode    # Point head to new node
        NewNode.prev = self.head    # Point new node back to hear

    def printQueue(self) -> None:
        myQueue = []
        CurrentNode = self.head.next
        while CurrentNode != self.tail:
            myQueue.append(CurrentNode.val)
            CurrentNode = CurrentNode.next 
        print( myQueue)
    
    def pop(self) -> int:

        if self.isEmpty():
            return -1
        RightNode = self.tail.prev   # Last node to pop
        PrevNode = RightNode.prev    # Node before
        self.tail.prev = PrevNode   # Assign tail to node before, skipping last node
        PrevNode.next = self.tail   # Assign node to tail

        return RightNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        LeftNode = self.head.next
        NextNode = LeftNode.next

        self.head.next = NextNode
        NextNode.prev = self.head
        return LeftNode.val