import os
from maze import *
from turtle import *
from datetime import datetime
''' File Name format student#_Name e.g.) 2015123456_John'''

''' Write a function to escape from a maze with searching algorithm'''
''' You are allowed to use 5 functions (Left, Right, Forward, Backward, isSuccess) with agent actions '''
''' Starting point will be given'''
''' Program will be tested with different maze'''

''' Comment is necessary for code description '''
''' Plagiarism prohibited '''
  
def escape():
    # Write a function to escape from a maze here
    print('Write a function to escape from a maze here')

if __name__ == '__main__':
    # Maze
    screen = Screen()
    sampleMaze()

    # Agent Init
    agent = Turtle()
    init_agent(agent)
    start = datetime.now()
    escape()
    finish = datetime.now()

    # Result
    print(os.path.basename(__file__).split('.')[0])
    print('Result   : Pass') if isSuccess() else print('Result   : Fail')
    print('Duration :', finish-start)

    mainloop()
