from EelemFringe import ElemFringe
from Fringe import Fringe
from Node import Node
from State import State
import labyrinth


def treeSearch():

    # initialization objects
    fringe = Fringe()
    state = State()
    node = Node(state, None, labyrinth.h[state.position])
    elemFringe = ElemFringe(node)
    fringe.addElem(elemFringe)
    i = 0

    while not fringe.isEmpty():
        elem = fringe.extract()
        print("Passo " + str(i) + ": " + str(elem.node.state.position) + "\n")
        if elem.node.state.checkGoalState():
            elem.node.printPath()
            break
        for neighbor in elem.node.state.getNeighborhood():
            newNode = Node(State(neighbor), elem.node, labyrinth.h[neighbor])
            elem.node.addChild(newNode)
            fringe.addElem(ElemFringe(newNode))
        i += 1


treeSearch()
