from Close import Close
from Open import Open
from Node import Node
from ElemList import ElemList
import labyrinth


def graphSearch():

    close = Close()
    open = Open()
    node = Node(None, None, None)
    node.h = labyrinth.h[node.position]
    elemList = ElemList(node)
    open.addElem(elemList)
    i = 0

    while not open.isEmpty():
        elemList = open.extract()
        print("Passo " + str(i) + ": " + str(elemList.node.position) + "\n")
        i += 1
        close.addElem(elemList)
        if elemList.node.checkGoalState():
            elemList.node.printPath()
            break
        else:
            for p in elemList.node.getNeighbors():
                node = Node(p, elemList.node, labyrinth.h[p])
                newElem = ElemList(node)
                if not close.isInClose(newElem):
                    open.addElem(newElem)


graphSearch()
