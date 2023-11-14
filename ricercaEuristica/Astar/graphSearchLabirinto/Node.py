import labyrinth


class Node:
    def __init__(self, position, parent, heuristic):
        if position == None:
            self.position = (4, 4)
        else:
            self.position = position
        self.parent = parent
        self.depth = 0
        self.h = heuristic
        self.children = []

    def addChild(self, child):
        self.children.append[child]
        child.parent = self
        child.depth = self.depth + 1

    def getNeighbors(self):
        return labyrinth.labyrinth[self.position]

    def printPath(self):
        if self.parent != None:
            self.parent.printPath(self.parent)

        print("->" + str(self.position))
