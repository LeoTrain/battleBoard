import pygame
import random
from typing import List, Tuple

    
def getCorrectImage(xPos: int, yPos: int, startingPos: Tuple[int, int], cellSize: Tuple[int, int], numOfCells: int) -> List[dict]:
    centerImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass.png").convert()
    centerImage = pygame.transform.scale(centerImage, cellSize)

    leftImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-left.png")
    leftImage = pygame.transform.scale(leftImage, cellSize)

    leftUpImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-up-left.png")
    leftUpImage = pygame.transform.scale(leftUpImage, cellSize)

    leftDownImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-down-left.png")
    leftDownImage = pygame.transform.scale(leftDownImage, cellSize)

    upImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-up.png")
    upImage = pygame.transform.scale(upImage, cellSize)

    rightUpImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-up-right.png")
    rightUpImage = pygame.transform.scale(rightUpImage, cellSize)

    rightImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-right.png")
    rightImage = pygame.transform.scale(rightImage, cellSize)

    rightDownImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-down-right.png")
    rightDownImage = pygame.transform.scale(rightDownImage, cellSize)

    downImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/grass-down.png")
    downImage = pygame.transform.scale(downImage, cellSize)

    
    image = None
    if xPos == startingPos[0] and yPos == startingPos[1]:
        image = leftUpImage  # Coin supérieur gauche
    elif xPos == startingPos[0] and yPos == startingPos[1] + (cellSize[1] * (numOfCells - 1)):
        image = leftDownImage  # Coin inférieur gauche
    elif xPos == startingPos[0] + (cellSize[0] * (numOfCells - 1)) and yPos == startingPos[1]:
        image = rightUpImage  # Coin supérieur droit
    elif xPos == startingPos[0] + (cellSize[0] * (numOfCells - 1)) and yPos == startingPos[1] + (cellSize[1] * (numOfCells - 1)):
        image = rightDownImage  # Coin inférieur droit
    elif xPos == startingPos[0]:
        image = leftImage  # Bord gauche
    elif xPos == startingPos[0] + (cellSize[0] * (numOfCells - 1)):
        image = rightImage  # Bord droit
    elif yPos == startingPos[1]:
        image = upImage  # Bord supérieur
    elif yPos == startingPos[1] + (cellSize[1] * (numOfCells - 1)):
        image = downImage  # Bord inférieur
    else:
        image = centerImage  # Centre
    
    return image

def getFloor(startingPos: Tuple[int, int], cellSize: Tuple[int, int], numOfCells: int) -> List[dict]:
    xPos, yPos = startingPos
    floor = []
    badCells = random.randint(20, 40)
    badCellImage = pygame.image.load("/Users/ftl/lab/battleBoard/sprites/badCell.png")
    badCellImage = pygame.transform.scale(badCellImage, cellSize)

    for i in range(numOfCells):
        xPos = startingPos[0]
        for j in range(numOfCells):
            rectangle = pygame.Rect(xPos, yPos, cellSize[0], cellSize[1])
            
            if badCells > 0:
                randomNumber = random.randint(1, 7)
                color = "red" if randomNumber == 4 else "blue"
                badCells -= 1 if color == "red" else 0
                image = badCellImage if color == "red" else getCorrectImage(xPos, yPos, startingPos, cellSize, numOfCells) 
            else:
                color = "blue"
                image = getCorrectImage(xPos, yPos, startingPos, cellSize, numOfCells)

                       
            floor.append({'rectangle': rectangle, 'color': color, 'image': image})
            xPos += cellSize[0]
        yPos += cellSize[1]
    return floor


def drawFloor(screen, floor):
    for cell in floor:
        screen.blit(cell['image'], cell['rectangle'])
        pygame.draw.rect(screen, 'black', cell['rectangle'], 1)

