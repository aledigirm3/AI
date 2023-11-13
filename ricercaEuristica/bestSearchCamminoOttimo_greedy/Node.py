class Node:
    def __init__(self, state, parent, h):
        self.state = state
        self.parent = parent
        self.h = h
        self.depth = 0
        self.children = []

    def addChild(self, childNode):
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1

    def printPath(self):
        if self.parent != None:
            self.parent.printPath()

        print('->' + self.state.name)
