import pygame
import random
from typing import List, Tuple
from player import Player

def createFloor(startingPos: Tuple[int, int]) -> List[dict]:
    posX, posY = startingPos
    floor = []
    badCells = random.randint(20, 40)
    for i in range(numCells):
        posX = startingPos[0]
        for i in range(numCells):
            rectangle = pygame.Rect(posX, posY, cellWidth, cellHeight)
            if badCells > 0:
                randomNumber = random.randint(1, 7)
                color = "red" if randomNumber == 4 else "blue"
                badCells -= 1 if color == "red" else 0
            else:
                color = "blue"
            floor.append({'rectangle': rectangle, 'color': color})
            posX += cellWidth
        posY += cellHeight
    return floor

def drawFloor(screen, floor):
    for cell in floor:
        pygame.draw.rect(screen, cell['color'], cell['rectangle'])
        pygame.draw.rect(screen, 'black', cell['rectangle'], 1)


pygame.init()

screenWidth = 1280
screenHeight = 720
screenSize = (screenWidth, screenHeight)

boardSize = 700
numCells = 10
cellSize = boardSize // numCells
cellWidth = cellSize
cellHeight = cellSize

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
running = True

startingX = (screenWidth - boardSize) // 2
startingY = (screenHeight - boardSize) // 2
startingPos = (startingX, startingY)
floor = createFloor(startingPos)

player = Player("yellow", cellWidth - 10, cellHeight - 10, (cellSize, cellSize), floor)
playerStartX = ((screenWidth - boardSize) // 2) + 5
playerStartY = ((screenHeight - boardSize) // 2) + 5
player.rect.topleft = (playerStartX, playerStartY)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if ((player.rect.left <= mousePos[0] & mousePos[0] <= player.rect.right) &
                (player.rect.top <= mousePos[1] & mousePos[1] <= player.rect.bottom)):
                if not player.selected:
                    player.selected = True
            elif player.selected == True:
                player.moove(mousePos)

    drawFloor(screen, floor)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

