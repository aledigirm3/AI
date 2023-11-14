class Fringe:
    def __init__(self):
        self.head = None
        self.tail = None

    def addElem(self, newElem):
        if self.head == None:
            self.head = newElem
            self.tail = newElem
        elif (self.head.node.h + self.head.node.depth) >= (newElem.node.h + newElem.node.depth):
            newElem.next = self.head
            self.head = newElem
        elif (self.tail.node.h + self.tail.node.depth) <= (newElem.node.h + newElem.node.depth):
            self.tail.next = newElem
            self.tail = newElem
        else:
            elem = self.head.next
            prevElem = self.head
            while elem != None:
                if (elem.node.h + elem.node.depth) >= (newElem.node.h + newElem.node.depth):
                    newElem.next = elem
                    prevElem.next = newElem
                    break
                elem = elem.next
                prevElem = prevElem.next

    def extract(self):
        elem = self.head
        self.head = self.head.next
        elem.next = None
        return elem

    def isEmpty(self):
        return self.head == None
