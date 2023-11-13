import map


class State:
    def __init__(self, name=None):
        if name == None:
            self.name = self.getInitialState()
        else:
            self.name = name

    def getInitialState(state):
        initialState = 'Arad'
        return initialState

    def successorFunction(self):
        return map.connections[self.name]

    def checkGoalState(self):
        return self.name == 'Bucarest'
