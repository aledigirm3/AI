from Game import Game
from GameAlphaBeta import GameAlphaBeta

game = Game()
gameAlphaBeta = GameAlphaBeta()


# game.play() #O(b^h), full tree visited
gameAlphaBeta.play()  # computationally optimized
