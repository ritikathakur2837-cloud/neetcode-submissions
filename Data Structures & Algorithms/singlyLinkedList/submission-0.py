class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next    
            i+= 1
        return -1

        

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode    

        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail =None
            return True
        prev = self.head
        curr = self.head.next
        i = 1
        while curr:
            if i== index:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False          
               
        

    def getValues(self) -> List[int]:
        res =[]
        curr =self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res    
        
