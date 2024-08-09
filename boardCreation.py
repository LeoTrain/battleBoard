import pygame
import random
from typing import List, Tuple

def getFloor(startingPos:Tuple[int, int], cellSize: Tuple[int, int], numOfCells: int) -> List[dict]:
    xPos, yPos = startingPos
    floor = []
    badCells = random.randint(20, 40)
    cellWidth = None
    for i in range(numOfCells):
        xPos = startingPos[0]
        for i in range(numOfCells):
            rectangle = pygame.Rect(xPos, yPos, cellSize[0], cellSize[1])
            if badCells > 0:
                randomNumber = random.randint(1, 7)
                color = "red" if randomNumber == 4 else "blue"
                badCells -= 1 if color == "red" else 0
            else:
                color = "blue"
            floor.append({'rectangle': rectangle, 'color': color})
            xPos += cellSize[0]
        yPos += cellSize[1]
    return floor

def drawFloor(screen, floor):
    for cell in floor:
        pygame.draw.rect(screen, cell['color'], cell['rectangle'])
        pygame.draw.rect(screen, 'black', cell['rectangle'], 1)
