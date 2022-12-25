import numpy as np
from time import sleep
import os
from threading import Thread
from _thread import interrupt_main
import sys

class Board:
    def __init__(self):
        self.board = np.zeros((9, 9))
        pass

    def load(self, board):
        self.board = board
        pass

    def printBoard(self):
        ic = 0
        jc = 0
        for i in range(11):
            if i == 4 or i == 8:
                ic += 1
            for j in range(11):
                if i == 3 or i == 7:
                    print("-", end="-")
                else:
                    if j == 3 or j == 7:
                        print("|", end=" ")
                        jc += 1
                    else:
                        if self.board[i - ic][j - jc] != -1:
                            print(int(self.board[i - ic][j - jc]), end=" ")
                        else:
                            print(" ", end=" ")
            jc = 0
            print("")
        pass

    def enterNumber(self, row, col, num):
        self.board[row-1][col-1] = num
        pass

class Render:
    def __init__(self, board, fps = 4):
        self.board = board
        self.fps = fps
        pass

    def drawSecond(self):
        delay = 1 / self.fps
        for i in range(self.fps):
            os.system('cls')
            self.board.printBoard()
            sleep(delay)
        pass

    def keyboard(self):
        val = input("Enter row, column and number(Syntax: 'row' 'column' 'number') to exit enter -1: ")

        if val == "-1":
            sys.exit(0)

        [row, col, number] = val.split()
        
        self.board.enterNumber(int(row), int(col), int(number))

        pass

    def gameLoop(self):
        try:
            # wait around
            while True:
                self.drawSecond()
        except KeyboardInterrupt:
            # terminate main thread
            self.keyboard()
            self.gameLoop()

class Game:
    def __init__(self):
        self.board = Board()
        self.render = Render(self.board)
        pass

    def board(self):
        return self.board

    def render(self):
        return self.render
