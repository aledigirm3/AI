from ElemFringe import ElemFringe
from Fringe import Fringe
from Node import Node
from State import State
import map


def Greedy_Best_First():

    # crea la frontiera
    fringe = Fringe()

    # crea lo stato iniziale
    initialState = State()

    # crea la radice
    euristica = map.h[initialState.name]
    # il nodo padre della radice è None
    root = Node(initialState, None, euristica)

    # aggiungi alla fringe
    elemento = ElemFringe(euristica, root)
    fringe.add(elemento)

    # se la fringe non è vuota ...
    while not fringe.empty_fringe():

        # estrazione dell'elemento in testa alla fringe
        elem_estratto = fringe.estrazione()
        currentNode = elem_estratto.node               # nodo estratto

        print("-- dequeue --", currentNode.state.name)

        # se lo stato del nodo estratto è lo stato obiettivo ...
        if currentNode.state.checkGoalState():
            print("Stato obiettivo raggiunto")
            print("----------------------")
            print("Soluzione:")
            # stampa il percorso trovato e termina l'elaborazione
            currentNode.printPath()
            break

        else:
            # espandi il nodo estratto ottenendo i suoi nodi figli
            childStates = currentNode.state.successorFunction()
            for childState in childStates:
                euristica = map.h[State(childState).name]
                childNode = Node(State(childState), currentNode, euristica)

                # aggiungi il nodo figlio alla lista dei figli del nodo corrente
                currentNode.addChild(childNode)

                # aggiungi il nodo figlio alla fringe
                elemento = ElemFringe(childNode.h, childNode)
                fringe.add(elemento)
            fringe.stampa()


Greedy_Best_First()
