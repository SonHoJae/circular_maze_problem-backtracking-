from maze import *
from turtle import *

''' Write a function to escape from a maze with searching algorithm'''
''' You are allowed to use 4 functions (Left, Right, Forward, Backward)'''
''' Comment is necessary for code description '''
''' Plagiarism prohibited '''
''' File Name format student#_Name e.g.) John_2015123456'''
def escape():
    Left(agent)
    Forward(agent)
    Forward(agent)
    Right(agent)
    Right(agent)
    Right(agent)
    Right(agent)
    Right(agent)
    Right(agent)
    Right(agent)
    Backward(agent)
    Right(agent)
    Backward(agent)
    Right(agent)
    Forward(agent)
    Right(agent)
    Forward(agent)
    Left(agent)
    Left(agent)
    Forward(agent)

if __name__ == '__main__':
    # Maze
    screen = Screen()  # create the screen
    sampleMaze()
    # Agent
    agent = Turtle()
    init_agent(agent)

    escape()
    mainloop()