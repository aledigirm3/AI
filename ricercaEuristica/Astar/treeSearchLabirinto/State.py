import labyrinth


class State:
    def __init__(self, position=None):
        if position == None:
            self.position = (4, 4)
        else:
            self.position = position

    def getNeighborhood(self):
        return labyrinth.labyrinth[(self.position)]

    def checkGoalState(self):
        return self.position == (1, 1)
