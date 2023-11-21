# from random string to "<goalString>" string with hill climbing algorithm (first choise)

import random
import string
import math


goalString = input("choose goalString: ")


def generate_random_string(length):
    return [random.choice(string.printable) for _ in range(length)]


def evaluate(solution):
    target = list(goalString)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        delta = abs(ord(s) - ord(t))
        diff = diff + delta
    return diff


def tweak(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)


toPrint = None


def hillClimbing():
    string = generate_random_string(len(goalString))
    toPrint = string
    currentEval = evaluate(string)
    i = 0
    while (currentEval != 0):
        newString = list(string)  # random
        tweak(newString)  # choise
        newEval = evaluate(newString)
        if (newEval < currentEval):
            print('Entra la stringa: ' + ''.join(newString) +
                  ' Con valore: ' + str(newEval) + '\n ITERATION: ' + str(i))
            string = newString
            currentEval = newEval
        i = i+1

    print('FROM:' + ''.join(toPrint) + ' TO:' + ''.join(goalString))


hillClimbing()
