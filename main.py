import pygame
import random
from typing import List, Tuple
from player import Player
from boardCreation import getFloor, drawFloor

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
floor = getFloor(startingPos, (cellSize, cellSize), numCells)

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

