# to track ElemList -> to visit

class Open:
    def __init__(self):
        self.head = None
        self.tail = None

        # sorted by heuristic function -> f = depth + h
    def addElem(self, newElem):
        if self.head == None:
            self.head = newElem
            self.tail = newElem
        elif self.tail.f <= newElem.f:
            self.tail.next = newElem
            self.tail = newElem
        elif self.head.f >= newElem.f:
            newElem.next = self.head
            self.head = newElem
        else:
            elem = self.head
            while elem.next != None:
                if (elem.next.f > newElem.f):
                    newElem.next = elem.next
                    elem.next = newElem
                    break

            elem = elem.next

    # fst elem
    def extract(self):
        elem = self.head
        self.head = elem.next
        elem.next = None
        return elem

    def isEmpty(self):
        return self.head == None
