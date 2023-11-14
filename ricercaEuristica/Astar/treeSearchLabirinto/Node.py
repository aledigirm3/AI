class Node:
    def __init__(self, state, parent, heuristic):
        self.state = state
        self.parent = parent
        self.h = heuristic
        self.depth = 0
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        self.depth += 1
        child.parent = self

    def printPath(self):
        if self.parent == None:
            print("->" + str(self.state.position))
        else:
            self.parent.printPath()
            print("->" + str(self.state.position))
