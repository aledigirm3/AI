# none can eat others

import random
import numpy as np
import math

n = 8


def tweak(sol):

    sol_copy = np.copy(sol)

    # scegli random due colonne distinte
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    while x == y:
        y = random.randint(0, n-1)

    # scambia le due colonne
    temp = sol_copy[y]
    sol_copy[y] = sol_copy[x]
    sol_copy[x] = temp

    return sol_copy


def initialization(sol):

    # shake shake shake
    for c in range(0, n-1):
        sol = tweak(sol)
    return sol


def printChess(sol):

    board = [[0] * n for i in range(n)]

    for x in range(0, n):
        board[sol[x]][x] = 'Q'
    print("SCACCHIERA", '\n')
    for x in range(0, n):
        for y in range(0, n):
            if (board[x][y] == 'Q'):
                print("Q   ", end=''),
            else:
                print(".   ", end=''),
        print("\n")
    print("\n\n")


def calculateConflict(chessB):

    # definizione della scacchiera N x N
    board = [[0] * n for i in range(n)]

    # inserimento delle regine ('Q') nelle loro posizioni sulla scacchiera
    for i in range(0, n):
        board[chessB[i]][i] = 'Q'

    # spostamenti possibili sulla scacchiera
    dx = [-1, 1, -1, 1]
    dy = [-1, 1, 1, -1]

    # inizializzazione numero di attacchi (diretti o indiretti)
    conflitti = 0

    for i in range(0, n):
        x = chessB[i]
        y = i

        # verifica attacchi sulle diagonali
        for j in range(0, 4):
            tempx = x
            tempy = y
            while (True):
                tempx = tempx + dx[j]           # move on x
                tempy = tempy + dy[j]           # move on y
                if ((tempx < 0) or
                    (tempx >= n) or
                    (tempy < 0) or
                        (tempy >= n)):
                    break                       # si esce se lo spostamento va fuori la scacchiera
                if (board[tempx][tempy] == 'Q'):
                    conflitti = conflitti + 1   # aggiornamento numero di attacchi
    return conflitti


# alpha for modify temperature
def simulatedAnnealing(temperaturaIniziale, temperaturaFinale, stepPerChange, alpha):
    temperatura = temperaturaIniziale
    currentState = initialization([0, 1, 2, 3, 4, 5, 6, 7])
    best = currentState
    printChess(best)
    while (temperatura > temperaturaFinale and calculateConflict(currentState) != 0):
        print('Temperatura: ' + str(temperatura))
        for step in range(stepPerChange):
            newState = tweak(currentState)
            # print(str(calculateConflict(currentState)) +
            #     ' -> ' + str(calculateConflict(newState)))
            if calculateConflict(newState) < calculateConflict(currentState):
                currentState = newState
                if calculateConflict(currentState) < calculateConflict(best):
                    best = currentState
            else:
                if random.random() <= math.exp(-((calculateConflict(newState) - calculateConflict(currentState)) / temperatura)):
                    currentState = newState

        temperatura *= alpha

    return best


printChess(simulatedAnnealing(30, 0.2, 100, 0.99))
