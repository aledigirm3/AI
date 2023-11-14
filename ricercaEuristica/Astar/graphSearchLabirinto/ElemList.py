
class ElemList:
    def __init__(self, node):
        self.node = node
        self.next = None
        # heuristic function
        self.f = node.h + node.depth
