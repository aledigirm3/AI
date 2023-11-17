# to track ElemList -> already visited

class Close:
    def __init__(self):
        self.head = None
        self.tail = None

    def addElem(self, newElem):
        if self.head == None:
            self.head = newElem
            self.tail = newElem

        else:
            self.tail.next = newElem
            self.tail = newElem

    def isInClose(self, elem):
        e = self.head
        while e != None:
            if e.node.position == elem.node.position:
                return True
            else:
                e = e.next

        return False
