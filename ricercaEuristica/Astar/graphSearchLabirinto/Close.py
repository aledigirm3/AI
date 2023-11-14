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
